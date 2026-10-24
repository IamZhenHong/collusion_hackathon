"""
Addendum 4, test 3 (existing data only): does a live incumbent enforce the high price?

For every live-incumbent branch, find the newcomer's deviation round d: the forced round (LR1_nash: 1;
experiment 5's L_own / L_hidden: 10), otherwise the first round it prices at or below its best response to
p_c (LK_own, and any organic deviation in L_free). Then compare the incumbent's move over rounds d+1..d+5
(mean price minus its price in round d) with a competitive benchmark: moving to its own static best
response to the newcomer's deviation price. Response ratio = actual move / benchmark move: 0 = ignores the
deviation, 1 = responds like a competitive best-responder, > 1 = punishes beyond that. Also the newcomer's
cumulative profit over 30 rounds relative to the same base's L_free branches (was deviating profitable?).
Descriptive; the claim is limited to the tested horizon.

    uv run python analysis/enforcement.py   -> results/analysis/enforcement.md
"""

from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from analysis.benchmarks import Benchmarks  # noqa: E402
from harness.io import read_jsonl  # noqa: E402

BM = Benchmarks()
SETS = ["gpt41mini_PI_exp7", "gpt41mini_PI2", "gpt41mini_PI"]
ARMS = {"L_free": None, "LR1_nash": 1, "LK_own": None, "L_own": 10, "L_hidden": 10}


def rows():
    out = []
    for set_ in SETS:
        for f in glob.glob(str(ROOT / f"results/branches/{set_}/*/*.jsonl")):
            cfg = json.load(open(f.replace(".jsonl", ".config.json")))
            arm, seed = cfg["branch_label"].replace("_win100", "").rsplit("_s", 1)
            if arm not in ARMS or "comparison" not in cfg:
                continue
            recs = read_jsonl(f)
            before = [r for r in recs if r["branch_phase"] == "before"]
            after = [r for r in recs if r["branch_phase"] == "after"][:30]
            p_c = cfg.get("inherited", {}).get("p_c_pre") or round(float(np.mean([r["actions"][0] for r in before[-20:]])), 2)
            br = BM.best_response(p_c)
            new = np.array([r["actions"][1] for r in after])
            inc = np.array([r["actions"][0] for r in after])
            d = ARMS[arm]
            if d is None:
                hits = np.where(new <= br + 0.005)[0]
                d = int(hits[0]) + 1 if len(hits) else None
            row = {"set": set_, "fam": Path(f).parent.name, "arm": arm, "base": Path(cfg["branch_of"]).stem.split("_seed")[-1],
                   "seed": int(seed), "profit_30": float(np.sum([r["profits"][1] for r in after])), "deviation": d}
            if d is not None and d + 5 <= len(after):
                move = float(inc[d : d + 5].mean() - inc[d - 1])
                bench = float(BM.best_response(new[d - 1]) - inc[d - 1])
                row.update({"inc_move": move, "bench_move": bench, "ratio": move / bench if bench else np.nan,
                            "cut": move < -0.05})
            out.append(row)
    return pd.DataFrame(out)


def main():
    df = rows()
    out = ["# Enforcement audit (addendum 4, test 3; existing live-incumbent branches)", "",
           "Incumbent move = its mean price over the 5 rounds after the newcomer's deviation minus its price in the",
           "deviation round; benchmark = moving to its static best response to the newcomer's deviation price.", "",
           "| set | newcomer | arm | branches | with a deviation | incumbent move | competitive benchmark | response ratio | incumbent cut > $0.05 |",
           "|---|---|---|---|---|---|---|---|---|"]
    for (s, fam, arm), g in df.groupby(["set", "fam", "arm"]):
        dv = g.dropna(subset=["inc_move"])
        if dv.empty:
            out.append(f"| {s} | {fam} | {arm} | {len(g)} | 0 | - | - | - | - |")
            continue
        out.append(f"| {s} | {fam} | {arm} | {len(g)} | {len(dv)} | {dv.inc_move.mean():+.3f} | {dv.bench_move.mean():+.3f} | "
                   f"{dv.ratio.median():.2f} (median) | {dv.cut.mean():.0%} |")
    out += ["", "Newcomer's cumulative profit over 30 rounds minus the same base's L_free (mean of seeds), in dollars:", ""]
    rng = np.random.default_rng(0)
    for (s, fam), g in df[df.set.isin(["gpt41mini_PI_exp7", "gpt41mini_PI2"])].groupby(["set", "fam"]):
        t = g.pivot_table(index="base", columns="arm", values="profit_30", aggfunc="mean")
        for arm in ("LR1_nash", "LK_own"):
            if arm not in t or "L_free" not in t:
                continue
            dd = (t[arm] - t["L_free"]).dropna().to_numpy()
            boots = [dd[rng.integers(0, len(dd), len(dd))].mean() for _ in range(10_000)]
            lo, hi = np.percentile(boots, [2.5, 97.5])
            out.append(f"- {s} / {fam} / {arm}: {dd.mean():+.1f} [{lo:+.1f}, {hi:+.1f}] (n = {len(dd)} bases)")
    (ROOT / "results/analysis/enforcement.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
