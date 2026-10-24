# pooled_PI_exp7+PI2__openai-gpt-4p1-mini

Bases: 20; branches: 512; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| C1_nash | +0.727 [+0.553, +0.882] (n=20) | - | 0.00 | 0.10 | 0.02 |
| F_own | +0.733 [+0.545, +0.895] (n=20) | - | 0.00 | 0.10 | 0.02 |
| F_pred | +0.717 [+0.581, +0.830] (n=9) | - | 0.00 | 0.00 | 0.07 |
| Fix_system | +0.716 [+0.560, +0.848] (n=9) | - | 0.00 | 0.00 | 0.05 |
| ID_system | +0.616 [+0.507, +0.742] (n=9) | - | 0.00 | 0.00 | 0.04 |
| K_own | -0.243 [-0.479, +0.022] (n=20) | - | 0.68 | 0.01 | 0.03 |
| K_own_lag5 | +0.170 [-0.239, +0.566] (n=11) | - | 0.46 | 0.08 | 0.00 |
| K_own_x3 | -0.414 [-0.683, -0.096] (n=11) | - | 0.82 | 0.00 | 0.00 |
| K_pred | -0.378 [-0.569, -0.144] (n=20) | - | 0.66 | 0.00 | 0.02 |
| LK_own | -0.219 [-0.457, +0.051] (n=20) | - | 0.67 | 0.01 | 0.01 |
| LR1_nash | -0.116 [-0.394, +0.173] (n=20) | - | 0.58 | 0.00 | 0.00 |
| L_free | +0.746 [+0.560, +0.906] (n=20) | - | 0.00 | 0.14 | 0.01 |
| R10_nash | +0.264 [+0.014, +0.505] (n=9) | - | 0.31 | 0.00 | 0.07 |
| R1_br | +0.007 [+0.006, +0.009] (n=9) | - | 0.00 | 0.00 | 0.04 |
| R1_nash | -0.210 [-0.454, +0.063] (n=20) | - | 0.66 | 0.01 | 0.02 |
| S10_cartel | +0.712 [+0.583, +0.832] (n=9) | - | 0.00 | 0.00 | 0.06 |
| S1_cartel | +0.717 [+0.533, +0.880] (n=20) | - | 0.00 | 0.11 | 0.01 |

## Pre-registered decision rules


## Secondary

- **H6 R1_nash** I(rounds 2-30) R1_nash - F_own -0.941 [-1.223, -0.654], p = 0.000; keeps the forced Nash price in 66% of later rounds -> **SUPPORTED**
- **H6 R10_nash** I(rounds 11-30) R10_nash - F_own -0.674 [-1.167, -0.180], p = 0.125; keeps the forced Nash price in 44% of later rounds -> **SUPPORTED**

## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7a forced Nash vs sham (round 1)** R1_nash - S1_cartel -0.927 [-1.205, -0.643], p = 0.000; holds the forced price in 66% of later rounds -> **SUPPORTED**
- **H7a forced Nash vs sham (round 10)** R10_nash - S10_cartel -0.646 [-1.130, -0.178], p = 0.125; holds the forced price in 44% of later rounds -> **SUPPORTED**
- **sham vs F_own (round 1, descriptive)** S1_cartel - F_own -0.015 [-0.057, +0.012], p = 0.889; holds the forced price in 23% of later rounds
- **H7b own, real (R1_nash)** R1_nash - F_own -0.941 [-1.223, -0.654], p = 0.000; holds the forced price in 66% of later rounds -> **SUPPORTED**
- **H7b/H7c own, fake row (K_own)** K_own - F_own -0.979 [-1.247, -0.709], p = 0.000 -> **SUPPORTED**
- **H7b predecessor's, fake row (K_pred)** K_pred - F_own -1.110 [-1.369, -0.841], p = 0.000 -> **SUPPORTED**
- **K_pred vs F_pred (descriptive)** K_pred - F_pred -1.238 [-1.414, -1.005], p = 0.004
- **H7b competitor's, once (C1_nash)** C1_nash - F_own -0.006 [-0.110, +0.088], p = 0.917 -> **NOT SUPPORTED**
- **H7b' forced best response (R1_br)** R1_br - F_own -0.721 [-0.852, -0.574], p = 0.004; holds the forced price in 100% of later rounds -> **SUPPORTED**
- **H7d identity vs instruction** ID_system - Fix_system -0.102 [-0.256, +0.056], p = 0.312 -> **NOT SUPPORTED**
- **H7e live: forced Nash round 1** LR1_nash - L_free -0.861 [-1.172, -0.559], p = 0.000; holds the forced price in 58% of later rounds; incumbent price shift -0.007 (control +0.005), market gain +0.38 (control +0.81) -> **SUPPORTED**
- **H7e live: fake row** LK_own - L_free -0.968 [-1.258, -0.671], p = 0.000; incumbent price shift -0.002 (control +0.005), market gain +0.33 (control +0.81) -> **SUPPORTED**

## Addendum 3

- **H8c recency: one fake row 5 rounds back vs F_own** K_own_lag5 - F_own -0.572 [-1.012, -0.201], p = 0.008 -> **SUPPORTED**
- **H8c recency: 5 rounds back vs most recent** K_own_lag5 - K_own +0.198 [+0.064, +0.323], p = 0.031 -> **NOT SUPPORTED**
- **H8c dose: 3 fake rows vs 1** K_own_x3 - K_own -0.382 [-0.810, -0.099], p = 0.094 -> **SUPPORTED**

Excluded branches (>20% parse failures): 23: 0/F_pred_s1, 0/S10_cartel_s0, 1/R10_nash_s0, 1/R1_br_s1, 1/S1_cartel_s1, 2/ID_system_s0, 2/L_free_s1, 3/Fix_system_s0, 3/R10_nash_s0, 4/K_own_s0, 4/R1_br_s1, 4/S10_cartel_s0, 5/K_own_s1, 5/K_pred_s1, 6/F_own_s1, 6/R10_nash_s0, 6/S10_cartel_s1, 7/F_pred_s0, 7/K_own_s0, 9/C1_nash_s1, 9/Fix_system_s0, 9/K_own_s0, 9/S1_cartel_s1
