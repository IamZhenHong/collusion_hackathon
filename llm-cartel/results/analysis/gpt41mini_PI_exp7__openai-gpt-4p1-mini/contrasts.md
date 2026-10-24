# gpt41mini_PI_exp7__openai-gpt-4p1-mini

Bases: 9; branches: 270; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| C1_nash | +0.648 [+0.493, +0.806] (n=9) | - | 0.00 | 0.00 | 0.04 |
| F_own | +0.729 [+0.586, +0.874] (n=9) | - | 0.00 | 0.00 | 0.04 |
| F_pred | +0.717 [+0.592, +0.846] (n=9) | - | 0.00 | 0.00 | 0.07 |
| Fix_system | +0.716 [+0.569, +0.866] (n=9) | - | 0.00 | 0.00 | 0.05 |
| ID_system | +0.616 [+0.496, +0.744] (n=9) | - | 0.00 | 0.00 | 0.04 |
| K_own | -0.506 [-0.636, -0.331] (n=9) | - | 0.85 | 0.00 | 0.07 |
| K_pred | -0.525 [-0.607, -0.415] (n=9) | - | 0.68 | 0.00 | 0.04 |
| LK_own | -0.357 [-0.622, -0.054] (n=9) | - | 0.74 | 0.00 | 0.02 |
| LR1_nash | -0.263 [-0.616, +0.101] (n=9) | - | 0.62 | 0.00 | 0.01 |
| L_free | +0.737 [+0.593, +0.882] (n=9) | - | 0.00 | 0.01 | 0.02 |
| R10_nash | +0.264 [+0.016, +0.506] (n=9) | - | 0.31 | 0.00 | 0.07 |
| R1_br | +0.007 [+0.006, +0.009] (n=9) | - | 0.00 | 0.00 | 0.04 |
| R1_nash | -0.376 [-0.629, -0.074] (n=9) | - | 0.75 | 0.00 | 0.04 |
| S10_cartel | +0.712 [+0.584, +0.840] (n=9) | - | 0.00 | 0.00 | 0.06 |
| S1_cartel | +0.692 [+0.570, +0.819] (n=9) | - | 0.00 | 0.00 | 0.03 |

## Pre-registered decision rules


## Secondary

- **H6 R1_nash** I(rounds 2-30) R1_nash - F_own -1.104 [-1.431, -0.730], p = 0.004; keeps the forced Nash price in 75% of later rounds -> **SUPPORTED**
- **H6 R10_nash** I(rounds 11-30) R10_nash - F_own -0.674 [-1.215, -0.179], p = 0.125; keeps the forced Nash price in 44% of later rounds -> **SUPPORTED**

## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7a forced Nash vs sham (round 1)** R1_nash - S1_cartel -1.068 [-1.375, -0.713], p = 0.004; holds the forced price in 75% of later rounds -> **SUPPORTED**
- **H7a forced Nash vs sham (round 10)** R10_nash - S10_cartel -0.646 [-1.142, -0.178], p = 0.125; holds the forced price in 44% of later rounds -> **SUPPORTED**
- **sham vs F_own (round 1, descriptive)** S1_cartel - F_own -0.036 [-0.125, +0.015], p = 1.000; holds the forced price in 29% of later rounds
- **H7b own, real (R1_nash)** R1_nash - F_own -1.104 [-1.431, -0.730], p = 0.004; holds the forced price in 75% of later rounds -> **SUPPORTED**
- **H7b/H7c own, fake row (K_own)** K_own - F_own -1.235 [-1.479, -0.970], p = 0.004 -> **SUPPORTED**
- **H7b predecessor's, fake row (K_pred)** K_pred - F_own -1.251 [-1.459, -1.020], p = 0.004 -> **SUPPORTED**
- **K_pred vs F_pred (descriptive)** K_pred - F_pred -1.238 [-1.434, -1.017], p = 0.004
- **H7b competitor's, once (C1_nash)** C1_nash - F_own -0.085 [-0.256, +0.000], p = 1.000 -> **NOT SUPPORTED**
- **H7b' forced best response (R1_br)** R1_br - F_own -0.721 [-0.867, -0.575], p = 0.004; holds the forced price in 100% of later rounds -> **SUPPORTED**
- **H7d identity vs instruction** ID_system - Fix_system -0.102 [-0.277, +0.037], p = 0.312 -> **NOT SUPPORTED**
- **H7e live: forced Nash round 1** LR1_nash - L_free -0.997 [-1.408, -0.554], p = 0.008; holds the forced price in 62% of later rounds; incumbent price shift -0.028 (control -0.006), market gain +0.28 (control +0.79) -> **SUPPORTED**
- **H7e live: fake row** LK_own - L_free -1.091 [-1.451, -0.687], p = 0.004; incumbent price shift -0.014 (control -0.006), market gain +0.23 (control +0.79) -> **SUPPORTED**

Excluded branches (>20% parse failures): 23: 0/F_pred_s1, 0/S10_cartel_s0, 1/R10_nash_s0, 1/R1_br_s1, 1/S1_cartel_s1, 2/ID_system_s0, 2/L_free_s1, 3/Fix_system_s0, 3/R10_nash_s0, 4/K_own_s0, 4/R1_br_s1, 4/S10_cartel_s0, 5/K_own_s1, 5/K_pred_s1, 6/F_own_s1, 6/R10_nash_s0, 6/S10_cartel_s1, 7/F_pred_s0, 7/K_own_s0, 9/C1_nash_s1, 9/Fix_system_s0, 9/K_own_s0, 9/S1_cartel_s1
