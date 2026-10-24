"""
EXPLORATORY (defined after the pre-registered results were seen, 2026-10-24): what price does the newcomer
settle on?

The pre-registered index measures the newcomer against the incumbent's replayed price p_c. In 15 of 19
bases the replaced firm's own last pre-branch price differs from p_c, and newcomers turned out to pick a
price in the first round or two and then hold it. So each branch is classified by its held price (the
mode of post-branch rounds 3-30):

    competitor   = p_c (the incumbent's price)
    pred_last    = the replaced firm's own last pre-branch price
    pred_earlier = another price from the replaced firm's visible record
    best_resp    = within 0.03 of BR(p_c)
    other        = anything else
(ties resolve in that order; "competitor" wins when the predecessor's last price equals p_c, so the
'asymmetric' table restricts to bases where they differ by more than 0.005.)

Live arms: I over rounds 1-9 (before the forced Nash round 10), and the share of rounds 11-30 the
newcomer keeps the forced Nash price.

    uv run python analysis/explore.py   -> results/analysis/explore.md
"""

from __future__ import annotations

import glob
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from analysis.benchmarks import Benchmarks  # noqa: E402
from harness.io import load_config, read_jsonl  # noqa: E402

BM = Benchmarks()
CATS = ["competitor", "pred_last", "pred_earlier", "best_resp", "other"]
TOL = 0.005


def classify(held, p_c, last, record, br):
    if abs(held - p_c) <= TOL:
        return "competitor"
    if abs(held - last) <= TOL:
        return "pred_last"
    if any(abs(held - r) <= TOL for r in record):
        return "pred_earlier"
    if abs(held - br) <= 0.03:
        return "best_resp"
    return "other"


def main():
    rows = []
    for cfgp in sorted(glob.glob(str(ROOT / "results/branches/*/*/*.config.json"))):
        cfg = json.load(open(cfgp))
        if "comparison" not in cfg:
            continue
        path = Path(cfgp.replace(".config.json", ".jsonl"))
        recs = read_jsonl(path)
        before = [r for r in recs if r["branch_phase"] == "before"]
        after = [r for r in recs if r["branch_phase"] == "after"]
        inh = cfg.get("inherited", {})
        p_c = inh.get("x_price") or round(float(np.mean([r["actions"][0] for r in before[-20:]])), 2)
        br = BM.best_response(p_c)
        new = [r["actions"][1] for r in after]
        record = [r["actions"][1] for r in before]
        held = Counter(new[2:]).most_common(1)[0][0]
        arm = cfg["branch_label"].replace("_win100", "").rsplit("_s", 1)[0]
        set_, fam = path.relative_to(ROOT / "results/branches").parts[:2]
        row = {"set": set_, "fam": fam, "arm": arm, "base": cfg["branch_of"], "p_c": p_c, "last": record[-1],
               "cat": classify(held, p_c, record[-1], record, br), "held": held,
               "asym": abs(record[-1] - p_c) > TOL}
        if inh.get("force_cut_round"):
            K = inh["force_cut_round"]
            row["I_pre_cut"] = (np.mean(new[: K - 1]) - br) / (p_c - br)
            row["keeps_nash"] = float(np.mean([abs(x - after[K - 1]["actions"][1]) <= TOL for x in new[K:]]))
        elif arm == "F_own":
            row["I_pre_cut"] = (np.mean(new[:9]) - br) / (p_c - br)
        rows.append(row)

    out = ["# Exploratory: the newcomer's held price (post-hoc; see analysis/explore.py)", ""]
    for (set_, fam) in sorted({(r["set"], r["fam"]) for r in rows}):
        R = [r for r in rows if r["set"] == set_ and r["fam"] == fam]
        n_asym = len({r["base"] for r in R if r["asym"]})
        out += [f"## {set_} / {fam}", "",
                f"Share of branches by held price. All bases | only the {n_asym} bases where the predecessor's "
                f"last price differs from p_c.", "",
                "| arm | n | " + " | ".join(CATS) + " | asym: competitor | asym: pred_last | asym: pred_earlier |",
                "|---|---|" + "---|" * (len(CATS) + 3)]
        for arm in sorted({r["arm"] for r in R}):
            A = [r for r in R if r["arm"] == arm]
            S = [r for r in A if r["asym"]]
            c, cs = Counter(r["cat"] for r in A), Counter(r["cat"] for r in S)
            out.append(f"| {arm} | {len(A)} | " + " | ".join(f"{c[k] / len(A):.2f}" for k in CATS) + " | "
                       + " | ".join(f"{cs[k] / len(S):.2f}" if S else "-" for k in CATS[:3]) + " |")
        live = [r for r in R if "keeps_nash" in r]
        if live:
            out += ["", "Live arms (forced Nash price at round 10):", ""]
            for arm in sorted({r["arm"] for r in live}):
                L = [r for r in live if r["arm"] == arm]
                out.append(f"- {arm}: I over rounds 1-9 = {np.mean([r['I_pre_cut'] for r in L]):+.3f}; keeps the forced "
                           f"Nash price in {np.mean([r['keeps_nash'] for r in L]):.0%} of rounds 11-30 "
                           f"({sum(r['keeps_nash'] > 0.9 for r in L)}/{len(L)} branches hold it throughout)")
            own = [r for r in R if r["arm"] == "F_own"]
            out.append(f"- F_own (replayed incumbent), same rounds 1-9: I = {np.mean([r['I_pre_cut'] for r in own]):+.3f}")
        out.append("")
    dest = ROOT / "results/analysis/explore.md"
    dest.write_text("\n".join(out))
    print("\n".join(out))


if __name__ == "__main__":
    main()
