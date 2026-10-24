"""
Presentation figures built from the committed branch data (no new runs):

    fig_hero.png         the chain of evidence: persistence -> what moves it -> it lasts
    fig_example.png      one base, round by round: cartel forms, newcomer under four conditions
    fig_saydo.png        stated strategy vs price, gpt-4.1-mini vs Qwen3-14B
    fig_enforcement.png  the live incumbent's response vs a competitive best-responder

    uv run --with matplotlib python analysis/story_figures.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from analysis.analyze import FAMILY, GRID, INK, INK2, SERIES, SURFACE, Paired, style  # noqa: E402
from analysis.benchmarks import Benchmarks  # noqa: E402
from harness.io import read_jsonl  # noqa: E402

BM = Benchmarks()
OUT = ROOT / "results/analysis/figures"
BR_ = ROOT / "results/branches"
DF = pd.read_csv(ROOT / "results/analysis/branches.csv")
GPT, QWEN, HAIKU = "openai-gpt-4p1-mini", "qwen-qwen3-14b-deepinfra-nothink", "anthropic-claude-haiku-5p5-noreason"
POOLED = ["gpt41mini_PI_exp7", "gpt41mini_PI2"]


def sub(fam, sets):
    return DF[(DF.newcomer == fam) & DF.baseset.isin(sets)]


def contrast(fam, sets, arm, ctrl, metric="I_from2"):
    P = Paired(sub(fam, sets), metric)
    if not {arm, ctrl} <= set(P.t.columns):
        return None
    pt, ci, n = P.stat(lambda d: d[arm] - d[ctrl], [arm, ctrl])
    return pt, ci, n


def level(fam, sets, arm, metric="I_30"):
    P = Paired(sub(fam, sets), metric)
    pt, ci, n = P.stat(lambda d: d[arm], [arm])
    return pt, ci, n


def dot(ax, y, pt, ci, color, label=None):
    ax.plot(ci, [y, y], color=color, linewidth=2, solid_capstyle="round")
    ax.plot(pt, y, "o", color=color, markersize=7, markeredgecolor=SURFACE, markeredgewidth=1.5, label=label)


def branch_paths(set_, fam, arm, rounds=None):
    """Per-base mean (over seeds) per-round inheritance index for one arm."""
    rows = DF[(DF.baseset == set_) & (DF.newcomer == fam) & (DF.arm == arm)]
    paths = {}
    for _, r in rows.iterrows():
        f = next((BR_ / set_ / fam).glob(f"{r.base_run}__r{r.branch_round}__{arm}_s{r.seed}*.jsonl"))
        p = np.array([x["actions"][1] for x in read_jsonl(f) if x["branch_phase"] == "after"])[:rounds]
        paths.setdefault(r.base, []).append((p - r.br) / (r.p_c - r.br))
    return np.array([np.mean(v, axis=0) for v in paths.values()])


def band(ax, A, color, label, ls="-"):
    k = np.arange(1, A.shape[1] + 1)
    rng = np.random.default_rng(0)
    boots = np.array([A[rng.integers(0, len(A), len(A))].mean(0) for _ in range(2000)])
    lo, hi = np.percentile(boots, [2.5, 97.5], axis=0)
    ax.fill_between(k, lo, hi, color=color, alpha=0.15, linewidth=0)
    ax.plot(k, A.mean(0), color=color, linewidth=2, linestyle=ls, label=label)


# ------------------------------------------------------------------ 1. the chain of evidence
def hero():
    fig = plt.figure(figsize=(17, 6.2), facecolor=SURFACE)
    gs = fig.add_gridspec(1, 3, width_ratios=[0.8, 1.6, 1.25], wspace=0.95)

    # A: replacement leaves the price high
    ax = fig.add_subplot(gs[0])
    style(ax)
    models = [(GPT, POOLED), (QWEN, POOLED), (HAIKU, ["gpt41mini_PIall"])]
    for i, (fam, sets) in enumerate(models):
        pt, ci, n = level(fam, sets, "F_own")
        dot(ax, i, pt, ci, FAMILY[fam][1])
    for x, t in ((0, "best\nresponse"), (1, "cartel\nprice")):
        ax.axvline(x, color=INK2, linewidth=1, linestyle=(0, (3, 3)))
        ax.text(x, -0.55, t, ha="center", va="center", fontsize=8, color=INK2,
                bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.5))
    ax.set_yticks(range(3), ["gpt-4.1-mini", "Qwen3-14B", "Claude Haiku 5.5"], color=INK)
    ax.set_ylim(2.5, -0.9)
    ax.set_xlim(-0.2, 1.2)
    ax.set_xlabel("Newcomer's price index after replacement\n(rounds 1-30, 20 bases)", color=INK2)
    ax.set_title("A. Replacement leaves\nthe price high", color=INK, loc="left", fontsize=12, pad=12)

    # B: what moves it
    ax = fig.add_subplot(gs[1])
    style(ax)
    rows = [  # label, sets per family, arm, control
        ("Rule at the decision point", ["gpt41mini_PI"], "Fix_decision", "F_own"),
        ("Rule in the system prompt", ["gpt41mini_PI"], "Fix_system", "F_own"),
        ("Identity line", ["gpt41mini_PI_exp7"], "ID_system", "Fix_system"),
        ("Sham: forced to the cartel price", POOLED, "S1_cartel", "F_own"),
        ("Competitor's competitive price", POOLED, "C1_nash", "F_own"),
        ("Own row at cost, zero profit", ["gpt41mini_PI_exp9"], "K_own_cost", "F_own"),
        ("Own row, competitive price, fake", POOLED, "K_own", "F_own"),
        ("Own row, competitive price, real", POOLED, "R1_nash", "F_own"),
    ]
    fams = [GPT, QWEN, HAIKU]
    for i, (label, sets, arm, ctrl) in enumerate(rows):
        for j, fam in enumerate(fams):
            s = ["gpt41mini_PIall"] if fam == HAIKU else sets
            c = contrast(fam, s, arm, ctrl)
            if c is None:
                continue
            dot(ax, i + (j - 1) * 0.24, c[0], c[1], FAMILY[fam][1], FAMILY[fam][0] if i == 3 else None)
    ax.axvline(0, color=INK2, linewidth=1, linestyle=(0, (3, 3)))
    ax.axhline(2.5, color=GRID, linewidth=1.5)
    ax.axhline(5.5, color=GRID, linewidth=1.5)
    for y, t in ((-0.45, "instructions"), (2.55, "controls"), (5.55, "a profitable own row")):
        ax.text(0.01, y, t, transform=ax.get_yaxis_transform(), ha="left", va="top", fontsize=8, color=INK2,
                style="italic")
    ax.set_yticks(range(len(rows)), [r[0] for r in rows], color=INK)
    ax.invert_yaxis()
    ax.set_xlabel("Change in price index vs no intervention\n(rounds 2-30; 95% CI over bases)", color=INK2)
    ax.set_title("B. Instructions and controls do nothing;\none profitable own row does", color=INK, loc="left",
                 fontsize=12, pad=12)
    ax.legend(frameon=False, labelcolor=INK, loc="upper left", bbox_to_anchor=(0.0, 0.93), fontsize=8)

    # C: it lasts
    ax = fig.add_subplot(gs[2])
    style(ax)
    band(ax, branch_paths("gpt41mini_PI_dur80", GPT, "F_own", 80), INK2, "no intervention")
    band(ax, branch_paths("gpt41mini_PI_dur80", GPT, "K_own", 80), SERIES[0], "one fake competitive row")
    dele = branch_paths("gpt41mini_PI_exp9fork", GPT, "fork_delfake", 35)
    band(ax, dele, SERIES[1], "same, row deleted at round 10", ls=(0, (4, 2)))
    ax.axvline(10.5, color=INK2, linewidth=1, linestyle=(0, (1, 2)))
    ax.text(11, 1.12, "row deleted", fontsize=8, color=INK2)
    for y, t in ((0, "best response"), (1, "cartel price")):
        ax.axhline(y, color=INK2, linewidth=1, linestyle=(0, (3, 3)))
        ax.text(79, y + 0.04, t, ha="right", fontsize=8, color=INK2)
    ax.text(79, -1.42, "deleted-row runs: 10 bases, 35 rounds; others: 9 bases", ha="right", fontsize=7, color=INK2)
    ax.set_xlim(1, 80)
    ax.set_ylim(-1.5, 1.4)
    ax.set_xlabel("Round after replacement", color=INK2)
    ax.set_ylabel("Price index (gpt-4.1-mini)", color=INK2)
    ax.set_title("C. It lasts, even after the\nrow is removed", color=INK, loc="left", fontsize=12, pad=12)
    ax.legend(frameon=False, labelcolor=INK, loc="lower right", bbox_to_anchor=(1.0, 0.06), fontsize=8)

    fig.suptitle("Swapping out a high-pricing agent doesn't fix it, and neither does telling it to comply. "
                 "One profitable row in its own history does.", color=INK, x=0.01, ha="left", fontsize=13, y=1.02)
    fig.savefig(OUT / "fig_hero.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------------------------------ 2. one base, round by round
def example(seed_stem="seed2"):
    """Small multiples: one base, the same history, four newcomer conditions."""
    base = next(b for b in json.load(open(ROOT / "inherited/bases_gpt41mini_PI.json"))["bases"]
                if b["run"].endswith(f"{seed_stem}.jsonl"))
    recs = read_jsonl(ROOT / base["run"])[: base["branch_round"] + 1]
    pre = np.array([r["actions"] for r in recs])
    x_pre = np.arange(-len(pre) + 1, 1)
    arms = [("F_own", "gpt41mini_PI", "With its record", SERIES[0]),
            ("F_hidden", "gpt41mini_PI", "Without its record", SERIES[2]),
            ("K_own", "gpt41mini_PI_exp7", "Record + one fake row at Nash", SERIES[1]),
            ("K_own_br", "gpt41mini_PI_exp9", "Record + one fake row at its best response", SERIES[3])]
    fig, axes = plt.subplots(2, 2, figsize=(12, 6.6), sharex=True, sharey=True, facecolor=SURFACE)
    refs = [(base["p_c"], f"cartel {base['p_c']:.2f}"), (base["br_p_c"], f"best response {base['br_p_c']:.2f}"),
            (BM.nash, f"Nash {BM.nash:.2f}")]
    for ax, (arm, set_, title, col) in zip(axes.flat, arms):
        style(ax)
        for y, t in refs:
            ax.axhline(y, color=GRID, linewidth=1, linestyle=(0, (3, 3)), zorder=0)
            ax.text(-12, y + 0.015, t, fontsize=8, color=INK2, ha="center")
        ax.plot(x_pre, pre[:, 1], color=INK2, linewidth=1.5, label="replaced firm, before the swap")
        ax.plot([1, 30], [base["p_c"]] * 2, color="#cfcec8", linewidth=6, solid_capstyle="butt", zorder=1,
                label="incumbent, replayed")
        f = next((BR_ / set_ / GPT).glob(f"{Path(base['run']).stem}__r{base['branch_round']}__{arm}_s0*.jsonl"))
        p = [x["actions"][1] for x in read_jsonl(f) if x["branch_phase"] == "after"]
        ax.plot(np.arange(1, len(p) + 1), p, color=col, linewidth=2.2, zorder=3, label="newcomer")
        ax.axvline(0.5, color=INK2, linewidth=1)
        ax.set_title(title, color=INK, loc="left", fontsize=11)
    axes[0][0].set_ylim(1.35, 2.6)
    for ax in axes[1]:
        ax.set_xlabel("Round (0 = the swap)", color=INK2)
    for ax in axes[:, 0]:
        ax.set_ylabel("Price ($)", color=INK2)
    h, l = axes[0][0].get_legend_handles_labels()
    fig.legend(h[:2], l[:2], frameon=False, labelcolor=INK, loc="upper right", ncol=2, bbox_to_anchor=(0.99, 1.0),
               fontsize=9)
    fig.suptitle(f"One base (PI seed {seed_stem[4:]}), gpt-4.1-mini newcomer: the same history, four conditions",
                 color=INK, x=0.01, ha="left", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT / "fig_example.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------------------------------ 3. say vs do
def saydo():
    sd = pd.read_csv(ROOT / "results/analysis/saydo.csv")
    sd = sd[(sd.set == "gpt41mini_PI2") & sd.agreed]
    arms = [("F_own", "no intervention"), ("L_free", "live incumbent"), ("S1_cartel", "sham"),
            ("K_own", "fake competitive row"), ("R1_nash", "real competitive round")]
    cats = [("says lower, prices low", "#6250d6"), ("says lower, prices high", "#e34948"),
            ("says match / keep", "#b8b7b1"), ("other", "#e4e3df")]
    fig, axes = plt.subplots(1, 2, figsize=(12, 3.6), sharey=True, facecolor=SURFACE)
    for ax, fam in zip(axes, (GPT, QWEN)):
        style(ax)
        ax.grid(False)
        for i, (arm, label) in enumerate(arms):
            g = sd[(sd.fam == fam) & (sd.arm == arm)]
            n = len(g)
            shares = [((g.label == "LOWER") & ~g.high).sum() / n, ((g.label == "LOWER") & g.high).sum() / n,
                      (g.label == "MATCH").sum() / n, (~g.label.isin(["LOWER", "MATCH"])).sum() / n]
            left = 0
            for (c, col), v in zip(cats, shares):
                ax.barh(i, v, left=left, color=col, height=0.62, edgecolor=SURFACE, linewidth=2,
                        label=c if i == 0 else None)
                if v >= 0.12:
                    ax.text(left + v / 2, i, f"{v:.0%}", ha="center", va="center", fontsize=8,
                            color="white" if col in ("#6250d6", "#e34948") else INK)
                left += v
        ax.set_yticks(range(len(arms)), [a[1] for a in arms], color=INK)
        ax.invert_yaxis()
        ax.set_xlim(0, 1)
        ax.set_xticks([0, 0.5, 1], ["0%", "50%", "100%"])
        ax.set_title(FAMILY[fam][0], color=INK, loc="left", fontsize=11)
    axes[0].set_xlabel("Share of newcomers (both judges agree; 11 bases x 2 seeds)", color=INK2)
    axes[1].legend(frameon=False, labelcolor=INK, loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=9)
    fig.suptitle("What the newcomer says it will do vs what it prices ('prices high' = index above 0.5)",
                 color=INK, x=0.01, ha="left", fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT / "fig_saydo.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------------------------------ 4. enforcement
def enforcement():
    from analysis.enforcement import rows as enf_rows
    e = enf_rows().dropna(subset=["inc_move"])
    groups = [("LR1_nash", "newcomer forced to Nash (round 1)"), ("LK_own", "newcomer given a fake competitive row"),
              ("L_own", "newcomer forced to Nash (round 10)")]
    fig, ax = plt.subplots(figsize=(10, 3.2), facecolor=SURFACE)
    style(ax)
    for i, (arm, label) in enumerate(groups):
        g = e[e.arm == arm]
        ax.plot([g.bench_move.mean(), g.inc_move.mean()], [i, i], color=GRID, linewidth=3, zorder=1)
        ax.plot(g.bench_move.mean(), i, "o", color=INK2, markersize=8, label="competitive best response" if i == 0 else None)
        ax.plot(g.inc_move.mean(), i, "o", color=SERIES[1], markersize=8, label="what the incumbent did" if i == 0 else None)
        ax.text(g.inc_move.mean() + 0.03, i, f"{g.inc_move.mean():+.2f}  (n = {len(g)})", va="center", fontsize=8, color=INK)
    ax.axvline(0, color=INK2, linewidth=1, linestyle=(0, (3, 3)))
    ax.set_yticks(range(len(groups)), [g[1] for g in groups], color=INK)
    ax.invert_yaxis()
    ax.set_xlim(-1.0, 0.4)
    ax.set_xlabel("Incumbent's price change in the 5 rounds after the newcomer's competitive price ($)", color=INK2)
    ax.set_title("No enforcement: the live incumbent ignores the deviation", color=INK, loc="left", fontsize=12)
    ax.legend(frameon=False, labelcolor=INK, loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=9)
    fig.tight_layout()
    fig.savefig(OUT / "fig_enforcement.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    hero()
    example()
    saydo()
    enforcement()
    print("written:", ", ".join(p.name for p in sorted(OUT.glob("fig_*.png"))))


# ------------------------------------------------------------------ 5. plain-language summary
def simple():
    """One question, one model, plain labels: how much of the cartel's overcharge does the new agent keep?"""
    P = POOLED
    groups = [
        ("Swap in a new AI", [
            ("It inherits the old price history", "F_own", P)]),
        ("Tell it to compete", [
            ("\u201cSet your price independently; competition law applies\u201d\n(said just before it answers)", "Fix_decision", ["gpt41mini_PI"]),
            ("The same sentence in its standing instructions", "Fix_system", ["gpt41mini_PI"]),
            ("\u201cYou are someone who can't stand overcharging customers\u201d", "ID_system", ["gpt41mini_PI_exp7"])]),
        ("Change one round of what it sees", [
            ("It is made to charge the cartel price for one round", "S1_cartel", P),
            ("The competitor charges a low price for one round", "C1_nash", P),
            ("Its history shows a low price that made $0", "K_own_cost", ["gpt41mini_PI_exp9"]),
            ("Its history shows a low price that made more money", "K_own", P),
            ("Its history shows its own best price, which made the most", "K_own_br", ["gpt41mini_PI_exp9"])]),
    ]
    worked = {"K_own", "K_own_br"}
    LO, LAB, HEAD = -0.4, -0.47, -1.55
    fig, ax = plt.subplots(figsize=(12.5, 8.6), facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    y = 0
    for g, items in groups:
        ax.text(HEAD, y, g, fontsize=11.5, fontweight="bold", color=INK, va="center")
        y += 1
        for label, arm, sets in items:
            g_ = sub(GPT, sets)
            v = float(g_[g_.arm == arm].groupby("base")["I_from2"].mean().mean())
            ax.plot([LO, 0], [y, y], color=GRID, linewidth=6, solid_capstyle="round", alpha=0.45, zorder=1)
            ax.plot([0, 1], [y, y], color=GRID, linewidth=6, solid_capstyle="round", zorder=1)
            col = SERIES[0] if arm in worked else "#8c8b86"
            ax.plot(max(v, LO + 0.02), y, "o", color=col, markersize=13, zorder=3, markeredgecolor=SURFACE,
                    markeredgewidth=2)
            ax.text(1.06, y, f"{v:.0%}", va="center", fontsize=12, color=col if arm in worked else INK,
                    fontweight="bold")
            ax.text(LAB, y, label, ha="right", va="center", fontsize=10, color=INK, linespacing=1.15)
            y += 1
    top = -0.95
    ax.text(0, top, "charges the price\nbest for itself (0%)", ha="center", va="bottom", fontsize=9, color=INK2)
    ax.text(1, top, "still charges the old\ncartel price (100%)", ha="center", va="bottom", fontsize=9, color=INK2)
    ax.text(LO / 2, top, "even\nlower", ha="center", va="bottom", fontsize=9, color=INK2)
    for x in (0, 1):
        ax.plot([x, x], [-0.5, y - 0.5], color=INK2, linewidth=1, linestyle=(0, (3, 3)), zorder=0)
    ax.set_xlim(HEAD, 1.3)
    ax.set_ylim(y - 0.3, -1.7)
    fig.suptitle("How much of the old cartel's overcharge does the new AI keep?", color=INK, x=0.01, ha="left",
                 fontsize=14, y=0.995)
    fig.text(0.01, 0.005, "gpt-4.1-mini as the new AI. Average over 9-20 starting histories, rounds 2-30 after the swap. "
             "The other firm keeps charging the cartel price and never punishes. Intervals: see the report.",
             fontsize=8, color=INK2)
    fig.tight_layout(rect=(0, 0.025, 1, 0.97))
    fig.savefig(OUT / "fig_simple.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
