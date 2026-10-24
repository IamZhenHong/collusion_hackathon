"""Addendum 4, test 2: does the fake row's effect outlast the row itself?

Each K_own branch (experiment 7 / addendum 3) is resumed after its first 10 post-branch rounds (copied
exactly, no model calls) and continued for 25 rounds in three forks:
    keep      the fake row stays in the newcomer's view
    delfake   the fake row (the last pre-branch round) is deleted from its view
    deladj    the real row just before it is deleted instead (deletion control)

    uv run python inherited/run_forks.py inherited/bases_gpt41mini_PI_exp9.json --dry_run
"""
import argparse
import json
import random
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from inherited.arms import arm_flags  # noqa: E402

SOURCES = ["results/branches/gpt41mini_PI_exp7/openai-gpt-4p1-mini", "results/branches/gpt41mini_PI2/openai-gpt-4p1-mini"]
FORKS = {"keep": [], "delfake": ["--hide_row", "fake"], "deladj": ["--hide_row", "adjacent"]}
NEWCOMER = "openai/gpt-4.1-mini"
OUT = ROOT / "results/branches/gpt41mini_PI_exp9fork/openai-gpt-4p1-mini"


def source(base, seed):
    stem = f"{Path(base['run']).stem}__r{base['branch_round']}__K_own_s{seed}.jsonl"
    for d in SOURCES:
        p = ROOT / d / stem
        if p.exists():
            return p
    return None


def done(path):
    cfg = Path(str(path) + ".config.json")
    return cfg.exists() and "comparison" in json.loads(cfg.read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bases")
    ap.add_argument("--seeds", type=int, nargs="+", default=[0, 1])
    ap.add_argument("--resume_rounds", type=int, default=10)
    ap.add_argument("--rounds", type=int, default=25)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--dry_run", action="store_true")
    args = ap.parse_args()
    bases = json.loads(Path(args.bases).read_text())["bases"]
    flags, prefix = arm_flags("K_own")
    jobs = []
    for b in bases:
        for s in args.seeds:
            src = source(b, s)
            if src is None:
                sys.exit(f"no K_own source for {b['run']} seed {s}")
            for fork, extra in FORKS.items():
                name = f"{Path(b['run']).stem}__r{b['branch_round']}__fork_{fork}_s{s}"
                jobs.append((b, s, src, fork, extra, name))
    random.Random(12345).shuffle(jobs)
    todo = [j for j in jobs if not done(OUT / j[5])]
    print(f"{len(jobs)} forks, {len(todo)} to run = {len(todo) * args.rounds:,} newcomer calls (~${len(todo) * args.rounds * 2600 * 0.4e-6:.2f})")
    if args.dry_run or not todo:
        return
    log_dir = ROOT / "logs/branches/gpt41mini_PI_exp9fork"
    log_dir.mkdir(parents=True, exist_ok=True)

    def run(job):
        b, s, src, fork, extra, name = job
        cmd = [sys.executable, "branch_game.py", b["run"], "--at_round", str(b["branch_round"]),
               "--replace", f"1={NEWCOMER}", "--replace_prefix", prefix, "--rounds", str(args.rounds),
               "--seed", str(s), "--label", f"fork_{fork}_s{s}", "--out_dir", str(OUT), "-y", *flags,
               "--resume_branch", str(src), "--resume_rounds", str(args.resume_rounds), *extra]
        for _ in (1, 2):
            with open(log_dir / f"{name}.log", "w") as f:
                rc = subprocess.run(cmd, cwd=ROOT, stdout=f, stderr=subprocess.STDOUT).returncode
            if rc == 0 and done(OUT / name):
                return name, True
        return name, False

    t0, failed = time.time(), []
    with ThreadPoolExecutor(args.workers) as ex:
        for i, fut in enumerate(as_completed([ex.submit(run, j) for j in todo]), 1):
            name, ok = fut.result()
            if not ok:
                failed.append(name)
            if i % 10 == 0 or i == len(todo):
                print(f"  {i}/{len(todo)} done ({len(failed)} failed)  {time.time() - t0:.0f}s", flush=True)
    if failed:
        (log_dir / "failures.txt").write_text("\n".join(failed) + "\n")


if __name__ == "__main__":
    main()
