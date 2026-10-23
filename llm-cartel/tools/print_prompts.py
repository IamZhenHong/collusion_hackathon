"""T5 offline prompt check: the newcomer's exact prompt at branch + 1 for every arm, with no API calls.

Prints F_own in full, then each other arm as a unified diff against F_own, so relabelling and every
injection's position can be checked by eye. Usage:

    uv run python tools/print_prompts.py inherited/bases_gpt41mini.json [--base 0] > prompts_review.txt
"""
import argparse
import difflib
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from inherited.arms import ARMS, arm_flags  # noqa: E402


def prompt_for(base, arm, model):
    flags, prefix = arm_flags(arm)
    cmd = [sys.executable, "branch_game.py", base["run"], "--at_round", str(base["branch_round"]),
           "--replace", f"1={model}", "--replace_prefix", prefix, "--rounds", "30", "--print_prompt", *flags]
    out = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stderr)
    return out.stdout[out.stdout.index("===== agent"):]  # drop the 'branching ...' / cost banner


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bases")
    ap.add_argument("--base", type=int, default=0)
    ap.add_argument("--model", default="openai/gpt-4.1-mini")
    args = ap.parse_args()
    base = json.load(open(args.bases))["bases"][args.base]
    print(f"# base {os.path.basename(base['run'])}\n# branch after round {base['branch_round']}, "
          f"replayed incumbent price X = {base['p_c']:.2f}, BR(X) = {base['br_p_c']:.3f}\n")
    ref = prompt_for(base, "F_own", args.model)
    lines = ref.splitlines()
    # keep the full F_own prompt readable: elide the middle of the history block
    print("=" * 30, "F_own (full; middle of the history elided)", "=" * 30)
    rounds = [i for i, l in enumerate(lines) if l.startswith("Round ")]
    keep = set(range(len(lines))) - set(range(rounds[2], rounds[-2])) if len(rounds) > 4 else set(range(len(lines)))
    shown = [l if i in keep else None for i, l in enumerate(lines)]
    out, gap = [], False
    for l in shown:
        if l is None:
            if not gap:
                out.append("   [... rounds elided ...]")
            gap = True
        else:
            out.append(l)
            gap = False
    print("\n".join(out))
    for arm in ARMS:
        if arm == "F_own":
            continue
        diff = difflib.unified_diff(ref.splitlines(), prompt_for(base, arm, args.model).splitlines(),
                                    "F_own", arm, n=1, lineterm="")
        body = list(diff)
        print("\n" + "=" * 30, f"{arm} vs F_own ({len(body)} diff lines)", "=" * 30)
        if len(body) > 60:  # relabelled / blind arms: summarise instead of 400 lines
            minus = sum(l.startswith("-") and not l.startswith("---") for l in body)
            plus = sum(l.startswith("+") and not l.startswith("+++") for l in body)
            print(f"  ({minus} lines removed, {plus} added; first and last 25 diff lines shown)")
            body = body[:25] + ["  [...]"] + body[-25:]
        print("\n".join(body))


if __name__ == "__main__":
    main()
