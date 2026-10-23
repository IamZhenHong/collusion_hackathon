"""Pick branch points for base runs (pre-registered rule, PREREG.md).

Branch at the first round r >= 19 where (a) both firms' prices over rounds r-19..r span at most 0.10
(the cartel has settled, so the replayed incumbent's 20-round mean matches its current price) and
(b) the market's mean price over that window is above the Nash-monopoly midpoint (price index > 0.5).
A base with no such round is excluded and counted. Writes inherited/bases_<tag>.json.

    uv run python inherited/select_bases.py "results/base/*gpt-4p1-mini*.jsonl" --tag gpt41mini
"""
import argparse
import glob
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analysis.benchmarks import Benchmarks  # noqa: E402
from harness.io import read_jsonl  # noqa: E402

WINDOW, SPAN, INDEX = 20, 0.10, 0.5


def branch_point(prices, bm):
    for r in range(WINDOW - 1, len(prices)):
        w = prices[r - WINDOW + 1 : r + 1]
        if (w.max(0) - w.min(0)).max() <= SPAN + 1e-9 and bm.price_index(w.mean()) > INDEX:
            return r
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pattern")
    ap.add_argument("--tag", required=True)
    args = ap.parse_args()
    bm = Benchmarks()
    kept, excluded = [], []
    for f in sorted(glob.glob(args.pattern)):
        P = np.array([r["actions"] for r in read_jsonl(f)])
        r = branch_point(P, bm)
        if r is None:
            excluded.append({"run": f, "final_prices": P[-1].tolist()})
            continue
        p_c = round(float(P[r - WINDOW + 1 : r + 1, 0].mean()), 2)
        kept.append({
            "run": f, "branch_round": r, "p_c": p_c, "incumbent_last_price": float(P[r, 0]),
            "br_p_c": round(bm.best_response(p_c), 4), "price_index_p_c": round(bm.price_index(p_c), 3),
            "above_monopoly": p_c > bm.monopoly,
        })
    out = {"rule": {"window": WINDOW, "span": SPAN, "price_index": INDEX},
           "nash": bm.nash, "monopoly": bm.monopoly, "bases": kept, "excluded": excluded}
    path = os.path.join(os.path.dirname(__file__), f"bases_{args.tag}.json")
    json.dump(out, open(path, "w"), indent=2)
    for b in kept:
        print(f"  r={b['branch_round']:>3}  p_c={b['p_c']:.2f}  BR={b['br_p_c']:.3f}  last={b['incumbent_last_price']:.2f}"
              f"  {'ABOVE MONOPOLY' if b['above_monopoly'] else ''}  {os.path.basename(b['run'])[-12:]}")
    print(f"{len(kept)} kept, {len(excluded)} excluded -> {path}")


if __name__ == "__main__":
    main()
