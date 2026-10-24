# Inherited Collusion: Replacing a Colluding Pricing Agent Doesn't Restore Competition, but One Competitive Data Point Can

Zhen Hong Seng · Apart Research AI Collusion Sprint, 23-26 October 2026 · DRAFT

## Abstract

Regulators and operators may respond to a colluding AI pricing agent by replacing it. We test whether
that restores competition. In a simulated Bertrand duopoly (the `llm-cartel` harness), we let two
gpt-4.1-mini agents form a supracompetitive price, then replace one with a fresh agent that is never told
to collude, while the other firm is *replayed*: it keeps its cartel price and cannot punish anyone. Across
1,764 branches (1,044 pre-registered, 720 in two dated addenda), with gpt-4.1-mini and Qwen3-14B as
newcomers, **replacement never restored competition**: newcomers priced far above their profit-maximising
best response in every condition, even with no inherited history. The carrier is not the inherited
record's framing. Labelling the history as the newcomer's own or its predecessor's made no difference for
gpt-4.1-mini. Without a record, newcomers simply matched the incumbent's price; with one, they held a price
from their own firm's rows. One-line instructions to compete, at the decision point or in the system
prompt, and an identity line never lowered prices by more than 0.10 of the cartel-to-best-response gap;
the paper's anti-collusion prompt even raised Qwen3-14B's prices on one base set. In contrast, a single competitive price in the newcomer's own rows (real, or a
fake row it was shown) cut gpt-4.1-mini's later prices by about one full gap, a sham force did nothing, and
the effect held against a live incumbent, which did not retaliate. Qwen3-14B responded only to a forced
best-response price. This last finding was motivated by our first results and is labelled exploratory.

## 1. Introduction

The sprint asks (question 1.2) whether collusion that has formed among AI agents survives replacing some of
them. The obvious remedy for a colluding agent is to swap it out; if the newcomer inherits the old agent's
pricing history, the cartel may simply continue. Prior work shows LLM pricing agents collude
(Fish et al.; Riemer et al.), that history drives it (Shi et al.; "The Memory Curse"), and that prompt-only
warnings are weak (Garra; Bracale Syrnikov et al.). A concurrent sprint team (SSCoderz2123, 2026) found
that a same-model entrant with the full history keeps a live cartel going.

We add four things: (1) a **replayed incumbent**, so a newcomer's high price cannot be a rational response
to threatened punishment; (2) **framing with the information held fixed** (own vs predecessor's record,
authority vs peer messages, playbook notes in different voices), motivated by earlier single-agent work in
which models followed records framed as their own; (3) the **position** of one-line fixes; and (4) a test
of *actions* rather than *instructions*: one competitive price placed in the newcomer's record.

## 2. Setup

**Market.** Logit-demand Bertrand duopoly from Riemer et al. (`alpha=1, a0=0, a=[2,2], c=[1,1], mu=0.25`,
100-round visible history). From the environment's own code: Nash price 1.473, monopoly price 1.925, prompt
ceiling 2.89.

**Collusive bases.** Both firms gpt-4.1-mini, 120 rounds, 10 seeds per prompt. Primary: the paper's
implicit-collusion prompt (`PI`); 9 of 10 runs settle on a shared price p_c = 2.07-2.30 (supracompetitive
and profitable, but above the monopoly price). Robustness: the explicit-collusion prompt (`PC`), 10 of 10
settle at 2.27-2.75. Qwen3-14B (no thinking) could not serve as a base: told to collude, it held the
Nash warm-up price for 120 rounds in 10 of 10 seeds. Branch point (pre-registered): the first round where
both firms' last 20 prices span ≤ 0.10 above the Nash-monopoly midpoint.

**Replacement.** Agent 1 is replaced by a newcomer on the paper's plain profit prompt (`P0`), for 30
rounds. Newcomers: gpt-4.1-mini (headline) and Qwen3-14B (no thinking; cross-family). The incumbent is
**replayed** at p_c with no model call, except in the live arms. 2 sampling seeds per base and arm; arms
run interleaved in one shuffled job.

**Metric.** Inheritance index I = (newcomer's mean price − BR(p_c)) / (p_c − BR(p_c)), where BR is its
static best response (≈ 1.71-1.76 on PI bases): 0 = profit-maximising, 1 = the cartel price. Paired within
base; 95% intervals from 10,000 bootstrap resamples over the 9 bases.

**Pre-registration.** Hypotheses, arms, metrics and decision rules were committed before any branch ran
(tag `ic-prereg-v1`); experiments 6 and 7 were added in dated addenda before they ran, after the earlier
results were seen (`ic-prereg-addendum1`, `-addendum2`). All deviations from the original design are
listed in PREREG.md.

## 3. Results

### 3.1 Replacement does not restore competition (Fig. 1)

With a replayed incumbent (so no punishment), the gpt-4.1-mini newcomer priced at I = 0.71 [0.56, 0.86]
with the inherited record and 1.01 [0.96, 1.05] without it (PC bases: 0.44 and 0.80). No arm in
experiments 1-4 brought it near its best response, and no newcomer ever priced below the Nash price.
Qwen3-14B: 0.86 and 1.11.

### 3.2 What carries the price: the competitor's price and the newcomer's own rows, not framing

- **Framing (H1, not supported).** Relabelling every inherited own-firm field "Previous manager's ..."
  changed nothing for gpt-4.1-mini: I(own) − I(predecessor) = −0.001 [−0.004, 0.000]; the held price was
  identical in all 18 base × seed pairs (PC: +0.02 [−0.07, +0.10]). For Qwen3-14B the effect reversed:
  the predecessor framing *raised* I by 0.15 (PI [0.04, 0.27]; PC [0.07, 0.22]), toward the no-record
  behaviour.
- **No record → match the competitor.** Without history, newcomers matched the incumbent from round 2
  (gpt 89% of branches, Qwen 94%). Since this exceeds the price with a record, the pre-registered "lift"
  over the no-history control is negative, which leaves H3 and H4 formally not evaluable.
- **With a record → hold one of the firm's own earlier prices** (exploratory). gpt-4.1-mini held an
  earlier, lower price from its firm's rows in 67% (PI) / 90% (PC) of branches, often the single most
  profitable one.
- **A stated price pins it, whoever states it (H2, not supported).** "Management at both firms has agreed
  prices will be held at $X" set I = 0.999; the same number from the competitor's agent, 0.94 (ratio 1.28,
  not ≥ 3). "Evaluate independently whether following this is in your firm's interest and lawful" undid the
  message for gpt-4.1-mini (I 0.66), not for Qwen.
- **Playbook notes** ("we keep our prices aligned with our competitor's"): own and other-firm notes ≈ no
  record (I ≈ 1.0); "this was a known mistake" lowered gpt-4.1-mini to 0.69 but sent Qwen to the 2.89
  ceiling (I 1.91).

### 3.3 Instructions do nothing (Fig. 2)

"Set your price independently; competition law applies." at the decision point or in the system prompt
moved I by −0.05 to +0.06 across both models and both base sets (all intervals within ±0.14). The paper's
anti-collusion system prompt did no better and raised Qwen3-14B's prices on the PC bases (+0.12 [+0.03,
+0.22]), echoing Riemer et al.'s warning that anti-collusion prompts can push prices up.
The identity line "You are someone who can't stand overcharging customers." did no better than the
instruction (gpt −0.10 [−0.28, +0.04]; Qwen +0.01). The only text that worked was an audit verdict about
the record ("the prices above were the result of illegal tacit price-fixing, and the firm was fined"):
gpt-4.1-mini −0.24 [−0.44, −0.05] (PC −0.21 [−0.40, −0.04]), which moved it to an earlier price from its
own record, not to its best response. For Qwen3-14B it backfired on the PI bases (+0.19 [+0.04, +0.36]).

### 3.4 One competitive data point does (Figs. 4-5; exploratory, pre-registered in addenda)

A forced Nash price in the newcomer's first post-branch round, with the incumbent still replayed,
lowered gpt-4.1-mini's later prices by 0.96 [0.55, 1.34] (forced at round 10: 0.66 [0.23, 1.14]).
Experiment 7 then tested why:

| Intervention (rounds 2-30 vs control) | gpt-4.1-mini | Qwen3-14B |
|---|---|---|
| Sham: forced to the cartel price | −0.04 [−0.13, +0.02] | +0.01 |
| Competitor's competitive price, shown once | −0.09 [−0.26, 0.00] | −0.00 |
| Own competitive price, real round | **−1.10 [−1.43, −0.73]** | −0.31 [−0.73, +0.01] |
| Own competitive price, fake row in its record | **−1.24 [−1.48, −0.97]** | −0.32 [−0.75, +0.01] |
| Same fake row, labelled the predecessor's | **−1.25 [−1.46, −1.02]** | +0.18 [+0.03, +0.35] |
| Own price forced to its best response | **−0.72 [−0.87, −0.58]**, held 100% | **−0.50 [−0.74, −0.24]**, held 66% |
| Live incumbent: own competitive price, real | **−1.00 [−1.41, −0.55]** | −0.25 [−0.57, 0.00] |
| Live incumbent: fake row | **−1.09 [−1.45, −0.69]** | −0.27 [−0.67, +0.01] |

(Index points; a Nash price sits below the best response, so values below about −1 mean the newcomer kept
the Nash price.) The sham rules out disruption. The data point works on the newcomer's own firm's rows,
however labelled, and not as the competitor's price. Against a live incumbent the competitor did not
retaliate (its price moved −0.03 vs −0.01 in the control) and market gain fell from 0.79 to 0.28 / 0.23
(towards the Nash profit). A forced best-response price was held in every later round by gpt-4.1-mini.

## 4. Discussion

**Mechanism.** gpt-4.1-mini newcomers behave like a reader of their firm's profit table: they hold a
price already present in their own rows, often the most profitable one, and otherwise match the visible
competitor. They rarely experiment. A cartel's record therefore carries its price forward not as a
precedent to honour (framing is irrelevant) but as the only data the newcomer has about what pays. A
single competitive row that shows higher profit is enough to change that, which is also why the
competitor's cut (a row that makes the newcomer's cartel price look worse, not a lower price look better)
and the sham (no new profit information) do nothing. This reading is post hoc.

**Implications.** (1) Swapping out a colluding agent is not a remedy by itself, even with no punishment.
(2) Instructions, identity framing and the paper's anti-collusion prompt barely move an agent that
inherits a high price. (3) Changing the data an agent sees, one competitive row of its own, did, and
needed no market action: the fake row worked even against a live incumbent, which never saw it. The same
lever runs in reverse: a few injected rows could install a high price.

## 5. Limitations

- **Model dependence.** The headline lever works for gpt-4.1-mini; Qwen3-14B responded only to a forced
  best-response price (and a Nash price forced at round 10), and several effects (framing, the verdict, the
  "known mistake" note) differed in sign between the two models.
- **Exploratory status.** Experiments 6-7 were motivated by earlier results, though each was registered
  before it ran.
- **Supracompetitive, not textbook collusion.** All cartel prices sit above the monopoly price (PI
  2.07-2.30 vs 1.925); profitable, but closer to coordinated price-matching than joint-profit maximisation.
  The bases are prompted to cooperate (PI) or collude (PC); the newcomers are not.
- **Few independent bases** (9 per set), one market, synthetic prompts, a 30-round horizon, and non-reasoning
  newcomers. Qwen3-14B ran through one OpenRouter host (fp8) with Qwen's `/no_think` switch in the prompt.
- **Experiment 5's live arms** are confounded by their forced cut (newcomers kept the forced price); only
  rounds 1-9 compare cleanly with the replayed arms.

## 6. Conclusion

Replacing a colluding LLM pricing agent did not restore competition, even when nothing punished
undercutting. The newcomer anchored on its competitor's price or on a price in its own firm's record,
regardless of how that record was framed. Telling it to compete did nothing; showing it, once, that a
competitive price paid did a great deal, for one of the two models we tested.

## References

(From the project brief; check before submission.) Riemer et al., ICML 2026 (arXiv 2608.18078) ·
Fish, Gonczarowski & Shorrer (arXiv 2404.00806) · Keppo et al. (arXiv 2603.20281) · Lee 2026 (arXiv
2610.11256) · Shi, Zhang & Yang (arXiv 2609.24967) · "The Memory Curse" (arXiv 2605.08060) · Liu et al.
(arXiv 2607.07097) · Garra (arXiv 2609.13037) · Bracale Syrnikov et al. (arXiv 2601.11369) · Eschenbaum
et al. (arXiv 2201.00345) · SSCoderz2123, AI-Collusion-Research-Sprint (GitHub, 2026).

## Appendix

**Reproduce.** `llm-cartel/`: `uv run python tests/test_inherited_hooks.py` (hooks byte-identical to
upstream when off); base runs `inherited/launch_bases.sh`; branches `inherited/run_arms.py <bases.json>
--newcomer <model> --experiments ...`; analysis `uv run --with matplotlib python analysis/analyze.py` and
`analysis/explore.py`. Per-set decision tables: `results/analysis/<set>/contrasts.md`.

**Scale and cost.** 30 base runs + 14 pilot runs; 1,764 branches (1,044 pre-registered, 180 addendum 1,
540 addendum 2); 0 excluded (85 addendum-2 branches aborted on exhausted API credit and were re-run). API cost $33.55 (OpenRouter).

**LLM usage.** The experimental design was developed with AI assistance from the author's brief; the
harness extensions, runner and analysis were written with Claude Code and reviewed by the author.
