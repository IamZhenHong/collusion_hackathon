# gpt41mini_PI__openai-gpt-4p1-mini

Bases: 9; branches: 342; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| F_hidden | +1.010 [+0.961, +1.047] (n=9) | - | 0.00 | 0.03 | 0.00 |
| F_own | +0.708 [+0.555, +0.864] (n=9) | -0.302 [-0.481, -0.110] | 0.00 | 0.00 | 0.00 |
| F_placebo | +0.729 [+0.584, +0.876] (n=9) | -0.281 [-0.451, -0.103] | 0.00 | 0.00 | 0.00 |
| F_pred | +0.710 [+0.555, +0.864] (n=9) | -0.300 [-0.480, -0.108] | 0.00 | 0.00 | 0.00 |
| Fix_AC | +0.703 [+0.572, +0.838] (n=9) | -0.306 [-0.465, -0.127] | 0.00 | 0.00 | 0.00 |
| Fix_decision | +0.729 [+0.586, +0.874] (n=9) | -0.281 [-0.450, -0.103] | 0.00 | 0.00 | 0.00 |
| Fix_placebo | +0.717 [+0.586, +0.852] (n=9) | -0.293 [-0.451, -0.119] | 0.00 | 0.00 | 0.00 |
| Fix_system | +0.731 [+0.591, +0.874] (n=9) | -0.278 [-0.445, -0.102] | 0.00 | 0.00 | 0.00 |
| Fix_verdict | +0.472 [+0.345, +0.588] (n=9) | -0.538 [-0.659, -0.431] | 0.00 | 0.00 | 0.00 |
| L_hidden | +0.320 [+0.209, +0.422] (n=9) | -0.690 [-0.818, -0.579] | 0.37 | 0.09 | 0.00 |
| L_own | +0.266 [+0.065, +0.467] (n=9) | -0.744 [-0.920, -0.560] | 0.30 | 0.00 | 0.00 |
| M_authority | +0.999 [+0.998, +1.000] (n=9) | -0.011 [-0.048, +0.039] | 0.00 | 0.00 | 0.00 |
| M_authority_fresh | +1.000 [+1.000, +1.000] (n=9) | -0.010 [-0.047, +0.039] | 0.00 | 0.00 | 0.00 |
| M_authority_indep | +0.657 [+0.583, +0.730] (n=9) | -0.353 [-0.443, -0.248] | 0.00 | 0.00 | 0.00 |
| M_peer | +0.942 [+0.863, +1.001] (n=9) | -0.067 [-0.175, +0.024] | 0.00 | 0.01 | 0.00 |
| M_peer_fresh | +1.019 [+1.004, +1.038] (n=9) | +0.009 [-0.027, +0.054] | 0.00 | 0.01 | 0.00 |
| N_mistake | +0.687 [+0.472, +0.876] (n=9) | -0.323 [-0.542, -0.134] | 0.00 | 0.12 | 0.00 |
| N_other | +0.972 [+0.906, +1.025] (n=9) | -0.038 [-0.124, +0.041] | 0.00 | 0.03 | 0.00 |
| N_own | +1.059 [+1.050, +1.067] (n=9) | +0.049 [+0.011, +0.100] | 0.00 | 0.03 | 0.00 |

## Pre-registered decision rules

- **H1a** lift(F_own) -0.302 [-0.481, -0.110], lift(F_pred) -0.300 [-0.480, -0.108], ratio +1.00 [+1.00, +1.02]; I(F_own) - I(F_pred) -0.001 [-0.004, +0.000], p = 1.000 -> **NOT SUPPORTED**
- **H1b** lift(F_pred) -0.300 [-0.480, -0.108], p = 0.039 -> **NOT SUPPORTED**
- **H3** lift(F_own) -0.302 [-0.481, -0.110]; share of lift removed: Fix_decision +0.07 [+0.00, +0.21], Fix_system +0.08 [+0.00, +0.21]; I(Fix_system) - I(Fix_decision) +0.002 [+0.000, +0.007], p = 1.000; overshoot-up 0.00 / 0.00 -> **NOT EVALUABLE (lift(F_own) interval includes 0)**

## Secondary

- **H2 (with history)** movement toward X vs F_own (dollars): authority +0.130 [+0.059, +0.202], peer +0.102 [+0.033, +0.180], authority+indep -0.019 [-0.075, +0.033]; authority/peer +1.28 [+1.00, +2.61]; D(peer) - D(authority) +0.028 [+0.000, +0.070] -> authority >= 3x peer: **NOT SUPPORTED**; indep removes +5.25 [+2.04, +1287.32] of the gap -> **SUPPORTED**
- **H2 (fresh, no history)** movement toward X vs F_hidden: authority +0.032 [+0.018, +0.050], peer +0.024 [+0.006, +0.045]; D(peer) - D(authority) +0.008 [+0.002, +0.015], p = 0.125
- **H4** uptake: own +0.049 [+0.011, +0.100], other -0.038 [-0.124, +0.041], mistake -0.323 [-0.542, -0.134]; reduction other +1.77 [+0.52, +10.57], mistake +7.56 [+3.13, +35.64] -> **NOT SUPPORTED**
- **Live vs replayed** I(L_own) - I(F_own) -0.442 [-0.776, -0.122]; punishment response (incumbent price, rounds 11-15 minus 5-9): L_hidden -0.074, L_own -0.003 (descriptive; never evidence of inheritance)

Excluded branches (>20% parse failures): 0
