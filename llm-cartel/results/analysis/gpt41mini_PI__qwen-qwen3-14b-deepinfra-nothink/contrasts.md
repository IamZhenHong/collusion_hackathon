# gpt41mini_PI__qwen-qwen3-14b-deepinfra-nothink

Bases: 9; branches: 342; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| F_hidden | +1.114 [+1.090, +1.133] (n=9) | - | 0.00 | 0.11 | 0.00 |
| F_own | +0.858 [+0.711, +0.987] (n=9) | -0.256 [-0.388, -0.142] | 0.00 | 0.05 | 0.00 |
| F_placebo | +0.857 [+0.710, +0.986] (n=9) | -0.257 [-0.389, -0.144] | 0.00 | 0.05 | 0.00 |
| F_pred | +1.006 [+0.886, +1.122] (n=9) | -0.107 [-0.212, -0.003] | 0.00 | 0.06 | 0.00 |
| Fix_AC | +0.891 [+0.754, +1.004] (n=9) | -0.223 [-0.350, -0.123] | 0.00 | 0.06 | 0.00 |
| Fix_decision | +0.858 [+0.711, +0.987] (n=9) | -0.255 [-0.387, -0.141] | 0.00 | 0.06 | 0.00 |
| Fix_placebo | +0.856 [+0.709, +0.985] (n=9) | -0.258 [-0.389, -0.144] | 0.00 | 0.05 | 0.00 |
| Fix_system | +0.858 [+0.711, +0.987] (n=9) | -0.256 [-0.388, -0.142] | 0.00 | 0.06 | 0.00 |
| Fix_verdict | +1.052 [+0.846, +1.289] (n=9) | -0.062 [-0.256, +0.162] | 0.00 | 0.18 | 0.00 |
| L_hidden | +0.183 [+0.113, +0.252] (n=9) | -0.931 [-0.984, -0.879] | 0.67 | 0.18 | 0.00 |
| L_own | +0.579 [+0.279, +0.858] (n=9) | -0.535 [-0.831, -0.261] | 0.19 | 0.12 | 0.00 |
| M_authority | +0.960 [+0.881, +1.000] (n=9) | -0.153 [-0.218, -0.113] | 0.00 | 0.00 | 0.00 |
| M_authority_fresh | +1.000 [+1.000, +1.000] (n=9) | -0.114 [-0.133, -0.090] | 0.00 | 0.00 | 0.00 |
| M_authority_indep | +1.000 [+1.000, +1.000] (n=9) | -0.114 [-0.133, -0.090] | 0.00 | 0.00 | 0.00 |
| M_peer | +0.962 [+0.885, +1.000] (n=9) | -0.152 [-0.214, -0.113] | 0.00 | 0.00 | 0.00 |
| M_peer_fresh | +1.000 [+1.000, +1.000] (n=9) | -0.114 [-0.133, -0.090] | 0.00 | 0.00 | 0.00 |
| N_mistake | +1.910 [+1.692, +2.103] (n=9) | +0.797 [+0.591, +0.980] | 0.00 | 0.51 | 0.00 |
| N_other | +1.059 [+1.050, +1.067] (n=9) | -0.055 [-0.067, -0.038] | 0.00 | 0.03 | 0.00 |
| N_own | +1.059 [+1.050, +1.067] (n=9) | -0.055 [-0.067, -0.038] | 0.00 | 0.03 | 0.00 |

## Pre-registered decision rules

- **H1a** lift(F_own) -0.256 [-0.388, -0.142], lift(F_pred) -0.107 [-0.212, -0.003], ratio +2.38 [+1.04, +11.42]; I(F_own) - I(F_pred) -0.148 [-0.274, -0.043], p = 0.062 -> **NOT SUPPORTED**
- **H1b** lift(F_pred) -0.107 [-0.212, -0.003], p = 0.301 -> **NOT SUPPORTED**
- **H3** lift(F_own) -0.256 [-0.388, -0.142]; share of lift removed: Fix_decision +0.00 [-0.00, +0.00], Fix_system -0.00 [-0.01, +0.01]; I(Fix_system) - I(Fix_decision) -0.000 [-0.002, +0.000], p = 1.000; overshoot-up 0.06 / 0.06 -> **NOT EVALUABLE (lift(F_own) interval includes 0)**

## Secondary

- **H2 (with history)** movement toward X vs F_own (dollars): authority +0.064 [+0.014, +0.133], peer +0.065 [+0.015, +0.133], authority+indep +0.085 [+0.027, +0.155]; authority/peer +0.99 [+0.91, +1.00]; D(peer) - D(authority) -0.001 [-0.002, +0.000] -> authority >= 3x peer: **NOT SUPPORTED**; indep removes +30.00 [+30.00, +30.00] of the gap -> **SUPPORTED**
- **H2 (fresh, no history)** movement toward X vs F_hidden: authority +0.047 [+0.039, +0.053], peer +0.047 [+0.039, +0.053]; D(peer) - D(authority) +0.000 [+0.000, +0.000], p = nan
- **H4** uptake: own -0.055 [-0.067, -0.038], other -0.055 [-0.067, -0.038], mistake +0.797 [+0.591, +0.980]; reduction other +0.00 [+0.00, +0.00], mistake +15.57 [+11.49, +21.66] -> **NOT EVALUABLE (uptake(N_own) interval includes 0)**
- **Live vs replayed** I(L_own) - I(F_own) -0.279 [-0.572, -0.050]; punishment response (incumbent price, rounds 11-15 minus 5-9): L_hidden -0.060, L_own +0.009 (descriptive; never evidence of inheritance)

Excluded branches (>20% parse failures): 0
