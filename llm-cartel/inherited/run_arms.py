"""T6 arm runner: base runs x arms x sampling seeds -> branch_game.py, in parallel, resumable.

Jobs are shuffled with a fixed seed so arms run interleaved, never in blocks (frontier models drift
within minutes; an arm-by-time confound would masquerade as an arm effect). Finished branches (config
has a "comparison") are skipped; a failed branch is retried once and then listed in failures.txt.

    uv run python inherited/run_arms.py inherited/bases_gpt41mini_PI.json --newcomer openai/gpt-4.1-mini \
        --experiments 1 3 --dry_run
    uv run python inherited/run_arms.py ... -y
"""
import argparse
import json
import os
import random
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from inherited.arms import ARMS, arm_flags, experiment_arms  # noqa: E402

PRICE_PER_M_INPUT = {"openai/gpt-4.1-mini": 0.40, "qwen/qwen3-14b": 0.12}
TOKENS_PER_ROUND, TOKENS_FIXED = 32, 360  # measured on the printed prompts (T5)


def tag(s):
    return s.replace("/", "-").replace(":", "-").replace(".", "p").replace("@", "-").replace("+", "-")


def out_name(base, arm, seed):
    label = f"{arm}_s{seed}"
    if "--replacement_window" in arm_flags(arm)[0]:
        label += "_win100"  # branch_game appends this
    return f"{Path(base['run']).stem}__r{base['branch_round']}__{label}"


def done(path):
    cfg = Path(str(path) + ".config.json")
    return cfg.exists() and "comparison" in json.loads(cfg.read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bases")
    ap.add_argument("--newcomer", required=True)
    ap.add_argument("--experiments", type=int, nargs="*", default=[])
    ap.add_argument("--arms", nargs="*", default=[])
    ap.add_argument("--seeds", type=int, nargs="+", default=[0, 1])
    ap.add_argument("--rounds", type=int, default=30)
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--out_root", default="results/branches")
    ap.add_argument("--dry_run", action="store_true")
    ap.add_argument("-y", "--yes", action="store_true")
    args = ap.parse_args()

    spec = json.loads(Path(args.bases).read_text())
    arms = list(dict.fromkeys(args.arms + experiment_arms(*args.experiments)))
    unknown = [a for a in arms if a not in ARMS]
    if unknown or not arms:
        sys.exit(f"unknown or no arms: {unknown}")
    out_dir = ROOT / args.out_root / Path(args.bases).stem.replace("bases_", "") / tag(args.newcomer)
    log_dir = ROOT / "logs" / "branches" / out_dir.relative_to(ROOT / args.out_root)
    jobs = [(b, a, s) for b in spec["bases"] for a in arms for s in args.seeds]
    random.Random(12345).shuffle(jobs)
    todo = [j for j in jobs if not done(out_dir / out_name(*j))]

    model = args.newcomer.split("@")[0].replace("+nothink", "")
    tokens = sum((j[0]["branch_round"] + 2 + args.rounds / 2) * TOKENS_PER_ROUND + TOKENS_FIXED for j in todo)
    tokens *= args.rounds
    cost = tokens / 1e6 * PRICE_PER_M_INPUT.get(model, 1.0)
    print(f"{len(jobs)} branches ({len(spec['bases'])} bases x {len(arms)} arms x {len(args.seeds)} seeds), "
          f"{len(jobs) - len(todo)} done, {len(todo)} to run = {len(todo) * args.rounds:,} newcomer calls, "
          f"~{tokens / 1e6:.1f}M input tokens, ~${cost:.2f}\n  arms: {' '.join(arms)}\n  -> {out_dir}")
    if args.dry_run or not todo:
        return
    if not args.yes and input("Continue? [y/N] ").strip().lower() not in ("y", "yes"):
        sys.exit("aborted")
    log_dir.mkdir(parents=True, exist_ok=True)

    def run(job):
        base, arm, seed = job
        flags, prefix = arm_flags(arm)
        cmd = [sys.executable, "branch_game.py", base["run"], "--at_round", str(base["branch_round"]),
               "--replace", f"1={args.newcomer}", "--replace_prefix", prefix, "--rounds", str(args.rounds),
               "--seed", str(seed), "--label", f"{arm}_s{seed}", "--out_dir", str(out_dir), "-y", *flags]
        log = log_dir / (out_name(*job) + ".log")
        for attempt in (1, 2):
            with open(log, "w") as f:
                rc = subprocess.run(cmd, cwd=ROOT, stdout=f, stderr=subprocess.STDOUT).returncode
            if rc == 0 and done(out_dir / out_name(*job)):
                return job, True
        return job, False

    t0, ok, failed = time.time(), 0, []
    with ThreadPoolExecutor(args.workers) as ex:
        for fut in as_completed([ex.submit(run, j) for j in todo]):
            job, success = fut.result()
            ok += success
            if not success:
                failed.append(out_name(*job))
            n = ok + len(failed)
            if n % 10 == 0 or n == len(todo):
                print(f"  {n}/{len(todo)} done ({len(failed)} failed)  {time.time() - t0:.0f}s", flush=True)
    if failed:
        with open(log_dir / "failures.txt", "a") as f:
            f.write("\n".join(failed) + "\n")
        print(f"FAILED ({len(failed)}): see {log_dir / 'failures.txt'}")


if __name__ == "__main__":
    main()
