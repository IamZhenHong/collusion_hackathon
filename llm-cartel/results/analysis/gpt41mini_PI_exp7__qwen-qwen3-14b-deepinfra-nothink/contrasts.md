# gpt41mini_PI_exp7__qwen-qwen3-14b-deepinfra-nothink

Bases: 9; branches: 270; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| C1_nash | +0.855 [+0.709, +0.982] (n=9) | - | 0.00 | 0.11 | 0.04 |
| F_own | +0.857 [+0.710, +0.987] (n=9) | - | 0.00 | 0.05 | 0.05 |
| F_pred | +1.006 [+0.886, +1.122] (n=9) | - | 0.00 | 0.06 | 0.06 |
| Fix_system | +0.858 [+0.711, +0.987] (n=9) | - | 0.00 | 0.06 | 0.05 |
| ID_system | +0.848 [+0.706, +0.972] (n=9) | - | 0.00 | 0.04 | 0.04 |
| K_own | +0.528 [+0.072, +0.906] (n=9) | - | 0.22 | 0.08 | 0.04 |
| K_pred | +1.037 [+0.881, +1.245] (n=9) | - | 0.00 | 0.15 | 0.03 |
| LK_own | +0.578 [+0.184, +0.905] (n=9) | - | 0.21 | 0.13 | 0.03 |
| LR1_nash | +0.607 [+0.236, +0.909] (n=9) | - | 0.18 | 0.12 | 0.02 |
| L_free | +0.859 [+0.711, +0.992] (n=9) | - | 0.00 | 0.13 | 0.03 |
| R10_nash | +0.512 [+0.194, +0.807] (n=9) | - | 0.23 | 0.04 | 0.03 |
| R1_br | +0.354 [+0.077, +0.675] (n=9) | - | 0.00 | 0.03 | 0.03 |
| R1_nash | +0.543 [+0.103, +0.908] (n=9) | - | 0.22 | 0.08 | 0.03 |
| S10_cartel | +0.856 [+0.709, +0.985] (n=9) | - | 0.00 | 0.04 | 0.07 |
| S1_cartel | +0.856 [+0.709, +0.984] (n=9) | - | 0.00 | 0.01 | 0.04 |

## Pre-registered decision rules


## Secondary

- **H6 R1_nash** I(rounds 2-30) R1_nash - F_own -0.306 [-0.732, +0.010], p = 0.625; keeps the forced Nash price in 22% of later rounds -> **NOT SUPPORTED**
- **H6 R10_nash** I(rounds 11-30) R10_nash - F_own -0.502 [-1.009, -0.127], p = 0.188; keeps the forced Nash price in 33% of later rounds -> **SUPPORTED**

## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7a forced Nash vs sham (round 1)** R1_nash - S1_cartel -0.313 [-0.738, +0.007], p = 0.375; holds the forced price in 22% of later rounds -> **NOT SUPPORTED**
- **H7a forced Nash vs sham (round 10)** R10_nash - S10_cartel -0.499 [-1.009, -0.118], p = 0.250; holds the forced price in 33% of later rounds -> **SUPPORTED**
- **sham vs F_own (round 1, descriptive)** S1_cartel - F_own +0.006 [-0.004, +0.017], p = 0.375; holds the forced price in 50% of later rounds
- **H7b own, real (R1_nash)** R1_nash - F_own -0.306 [-0.732, +0.010], p = 0.625; holds the forced price in 22% of later rounds -> **NOT SUPPORTED**
- **H7b/H7c own, fake row (K_own)** K_own - F_own -0.322 [-0.748, +0.008], p = 0.562 -> **NOT SUPPORTED**
- **H7b predecessor's, fake row (K_pred)** K_pred - F_own +0.183 [+0.026, +0.353], p = 0.062 -> **NOT SUPPORTED**
- **K_pred vs F_pred (descriptive)** K_pred - F_pred +0.040 [-0.055, +0.170], p = 0.750
- **H7b competitor's, once (C1_nash)** C1_nash - F_own -0.002 [-0.013, +0.009], p = 0.750 -> **NOT SUPPORTED**
- **H7b' forced best response (R1_br)** R1_br - F_own -0.496 [-0.737, -0.243], p = 0.008; holds the forced price in 66% of later rounds -> **SUPPORTED**
- **H7d identity vs instruction** ID_system - Fix_system +0.006 [-0.005, +0.023], p = 1.000 -> **NOT SUPPORTED**
- **H7e live: forced Nash round 1** LR1_nash - L_free -0.245 [-0.567, +0.004], p = 0.375; holds the forced price in 18% of later rounds; incumbent price shift +0.024 (control +0.024), market gain +0.59 (control +0.73) -> **NOT SUPPORTED**
- **H7e live: fake row** LK_own - L_free -0.272 [-0.674, +0.005], p = 0.438; incumbent price shift +0.017 (control +0.024), market gain +0.58 (control +0.73) -> **NOT SUPPORTED**

Excluded branches (>20% parse failures): 5: 0/F_own_s0, 5/LK_own_s0, 5/L_free_s0, 5/R10_nash_s1, 7/S10_cartel_s1
