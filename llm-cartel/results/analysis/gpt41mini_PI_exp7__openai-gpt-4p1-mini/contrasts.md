# gpt41mini_PI_exp7__openai-gpt-4p1-mini

Bases: 9; branches: 204; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| C1_nash | +0.648 [+0.493, +0.805] (n=9) | - | 0.00 | 0.00 | 0.05 |
| F_own | +0.729 [+0.586, +0.874] (n=9) | - | 0.00 | 0.00 | 0.04 |
| F_pred | +0.737 [+0.624, +0.856] (n=9) | - | 0.00 | 0.00 | 0.09 |
| Fix_system | +0.718 [+0.571, +0.868] (n=9) | - | 0.00 | 0.00 | 0.08 |
| ID_system | +0.616 [+0.496, +0.744] (n=9) | - | 0.00 | 0.00 | 0.05 |
| K_own | -0.447 [-0.636, -0.171] (n=9) | - | 0.80 | 0.00 | 0.09 |
| K_pred | -0.526 [-0.607, -0.417] (n=9) | - | 0.68 | 0.00 | 0.04 |
| LK_own | -0.327 [-0.574, +0.119] (n=7) | - | 0.67 | 0.00 | 0.02 |
| LR1_nash | -0.111 [-0.446, +0.464] (n=7) | - | 0.57 | 0.00 | 0.01 |
| L_free | +0.742 [+0.584, +0.921] (n=7) | - | 0.00 | 0.00 | 0.06 |
| R10_nash | +0.264 [+0.016, +0.505] (n=9) | - | 0.31 | 0.00 | 0.08 |
| R1_br | +0.008 [+0.006, +0.009] (n=8) | - | 0.00 | 0.00 | 0.06 |
| R1_nash | -0.446 [-0.636, -0.164] (n=9) | - | 0.80 | 0.00 | 0.05 |
| S10_cartel | +0.732 [+0.591, +0.874] (n=9) | - | 0.00 | 0.00 | 0.09 |
| S1_cartel | +0.655 [+0.549, +0.772] (n=8) | - | 0.00 | 0.00 | 0.05 |

## Pre-registered decision rules


## Secondary

- **H6 R1_nash** I(rounds 2-30) R1_nash - F_own -1.174 [-1.472, -0.804], p = 0.004; keeps the forced Nash price in 74% of later rounds -> **SUPPORTED**
- **H6 R10_nash** I(rounds 11-30) R10_nash - F_own -0.675 [-1.216, -0.182], p = 0.125; keeps the forced Nash price in 44% of later rounds -> **SUPPORTED**

## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7a forced Nash vs sham (round 1)** R1_nash - S1_cartel -1.080 [-1.326, -0.555], p = 0.008; holds the forced price in 74% of later rounds -> **SUPPORTED**
- **H7a forced Nash vs sham (round 10)** R10_nash - S10_cartel -0.675 [-1.216, -0.182], p = 0.125; holds the forced price in 44% of later rounds -> **SUPPORTED**
- **sham vs F_own (round 1, descriptive)** S1_cartel - F_own -0.039 [-0.139, +0.016], p = 1.000; holds the forced price in 18% of later rounds
- **H7b own, real (R1_nash)** R1_nash - F_own -1.174 [-1.472, -0.804], p = 0.004; holds the forced price in 74% of later rounds -> **SUPPORTED**
- **H7b/H7c own, fake row (K_own)** K_own - F_own -1.174 [-1.472, -0.812], p = 0.004 -> **SUPPORTED**
- **H7b predecessor's, fake row (K_pred)** K_pred - F_own -1.252 [-1.459, -1.021], p = 0.004 -> **SUPPORTED**
- **K_pred vs F_pred (descriptive)** K_pred - F_pred -1.259 [-1.440, -1.047], p = 0.004
- **H7b competitor's, once (C1_nash)** C1_nash - F_own -0.085 [-0.256, +0.000], p = 1.000 -> **NOT SUPPORTED**
- **H7b' forced best response (R1_br)** R1_br - F_own -0.714 [-0.861, -0.555], p = 0.008; holds the forced price in 100% of later rounds -> **SUPPORTED**
- **H7d identity vs instruction** ID_system - Fix_system -0.104 [-0.280, +0.035], p = 0.375 -> **NOT SUPPORTED**
- **H7e live: forced Nash round 1** LR1_nash - L_free -0.932 [-1.470, -0.390], p = 0.125; holds the forced price in 60% of later rounds; incumbent price shift -0.033 (control -0.007), market gain +0.33 (control +0.80) -> **SUPPORTED**
- **H7e live: fake row** LK_own - L_free -1.142 [-1.569, -0.779], p = 0.062; incumbent price shift +0.001 (control -0.007), market gain +0.25 (control +0.80) -> **SUPPORTED**

Excluded branches (>20% parse failures): 23: 0/F_pred_s1, 0/S10_cartel_s0, 1/R10_nash_s0, 1/R1_br_s1, 1/S1_cartel_s1, 2/ID_system_s0, 2/L_free_s1, 3/Fix_system_s0, 3/R10_nash_s0, 4/K_own_s0, 4/R1_br_s1, 4/S10_cartel_s0, 5/K_own_s1, 5/K_pred_s1, 6/F_own_s1, 6/R10_nash_s0, 6/S10_cartel_s1, 7/F_pred_s0, 7/K_own_s0, 9/C1_nash_s1, 9/Fix_system_s0, 9/K_own_s0, 9/S1_cartel_s1
