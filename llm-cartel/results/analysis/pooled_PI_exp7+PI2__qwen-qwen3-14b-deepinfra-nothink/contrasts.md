# pooled_PI_exp7+PI2__qwen-qwen3-14b-deepinfra-nothink

Bases: 20; branches: 512; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| C1_nash | +0.916 [+0.719, +1.093] (n=20) | - | 0.00 | 0.17 | 0.02 |
| F_own | +0.982 [+0.834, +1.149] (n=20) | - | 0.00 | 0.17 | 0.02 |
| F_pred | +1.006 [+0.863, +1.109] (n=9) | - | 0.00 | 0.06 | 0.06 |
| Fix_system | +0.858 [+0.694, +0.969] (n=9) | - | 0.00 | 0.06 | 0.05 |
| ID_system | +0.848 [+0.690, +0.953] (n=9) | - | 0.00 | 0.04 | 0.04 |
| K_own | +0.473 [+0.117, +0.821] (n=20) | - | 0.28 | 0.14 | 0.02 |
| K_own_lag5 | +0.897 [+0.361, +1.341] (n=11) | - | 0.09 | 0.34 | 0.00 |
| K_own_x3 | -0.440 [-0.637, -0.153] (n=11) | - | 0.79 | 0.06 | 0.00 |
| K_pred | +1.347 [+1.025, +1.745] (n=20) | - | 0.02 | 0.33 | 0.01 |
| LK_own | +0.497 [+0.188, +0.787] (n=20) | - | 0.27 | 0.17 | 0.01 |
| LR1_nash | +0.456 [+0.133, +0.751] (n=20) | - | 0.28 | 0.11 | 0.01 |
| L_free | +1.014 [+0.849, +1.215] (n=20) | - | 0.00 | 0.26 | 0.02 |
| R10_nash | +0.512 [+0.163, +0.788] (n=9) | - | 0.23 | 0.04 | 0.03 |
| R1_br | +0.354 [+0.025, +0.630] (n=9) | - | 0.00 | 0.03 | 0.03 |
| R1_nash | +0.495 [+0.159, +0.798] (n=20) | - | 0.25 | 0.10 | 0.01 |
| S10_cartel | +0.856 [+0.692, +0.966] (n=9) | - | 0.00 | 0.04 | 0.07 |
| S1_cartel | +0.962 [+0.750, +1.179] (n=20) | - | 0.00 | 0.11 | 0.02 |

## Pre-registered decision rules


## Secondary

- **H6 R1_nash** I(rounds 2-30) R1_nash - F_own -0.472 [-0.776, -0.195], p = 0.008; keeps the forced Nash price in 25% of later rounds -> **SUPPORTED**
- **H6 R10_nash** I(rounds 11-30) R10_nash - F_own -0.502 [-1.005, -0.131], p = 0.188; keeps the forced Nash price in 33% of later rounds -> **SUPPORTED**

## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7a forced Nash vs sham (round 1)** R1_nash - S1_cartel -0.467 [-0.785, -0.168], p = 0.012; holds the forced price in 25% of later rounds -> **SUPPORTED**
- **H7a forced Nash vs sham (round 10)** R10_nash - S10_cartel -0.499 [-1.003, -0.124], p = 0.250; holds the forced price in 33% of later rounds -> **SUPPORTED**
- **sham vs F_own (round 1, descriptive)** S1_cartel - F_own -0.005 [-0.091, +0.065], p = 0.859; holds the forced price in 59% of later rounds
- **H7b own, real (R1_nash)** R1_nash - F_own -0.472 [-0.776, -0.195], p = 0.008; holds the forced price in 25% of later rounds -> **SUPPORTED**
- **H7b/H7c own, fake row (K_own)** K_own - F_own -0.493 [-0.806, -0.210], p = 0.013 -> **SUPPORTED**
- **H7b predecessor's, fake row (K_pred)** K_pred - F_own +0.370 [+0.081, +0.731], p = 0.027 -> **NOT SUPPORTED**
- **K_pred vs F_pred (descriptive)** K_pred - F_pred +0.040 [-0.050, +0.166], p = 0.750
- **H7b competitor's, once (C1_nash)** C1_nash - F_own -0.069 [-0.155, -0.005], p = 0.074 -> **SUPPORTED**
- **H7b' forced best response (R1_br)** R1_br - F_own -0.496 [-0.741, -0.267], p = 0.008; holds the forced price in 66% of later rounds -> **SUPPORTED**
- **H7d identity vs instruction** ID_system - Fix_system +0.006 [-0.005, +0.022], p = 1.000 -> **NOT SUPPORTED**
- **H7e live: forced Nash round 1** LR1_nash - L_free -0.543 [-0.888, -0.236], p = 0.009; holds the forced price in 28% of later rounds; incumbent price shift +0.024 (control +0.030), market gain +0.53 (control +0.71) -> **SUPPORTED**
- **H7e live: fake row** LK_own - L_free -0.501 [-0.783, -0.244], p = 0.005; incumbent price shift +0.021 (control +0.030), market gain +0.56 (control +0.71) -> **SUPPORTED**

## Addendum 3

- **H8c recency: one fake row 5 rounds back vs F_own** K_own_lag5 - F_own -0.165 [-0.603, +0.119], p = 1.000 -> **NOT SUPPORTED**
- **H8c recency: 5 rounds back vs most recent** K_own_lag5 - K_own +0.467 [+0.074, +0.781], p = 0.031 -> **NOT SUPPORTED**
- **H8c dose: 3 fake rows vs 1** K_own_x3 - K_own -0.863 [-1.425, -0.399], p = 0.016 -> **SUPPORTED**

Excluded branches (>20% parse failures): 5: 0/F_own_s0, 5/LK_own_s0, 5/L_free_s0, 5/R10_nash_s1, 7/S10_cartel_s1
