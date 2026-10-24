# gpt41mini_PI2__qwen-qwen3-14b-deepinfra-nothink

Bases: 11; branches: 242; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| C1_nash | +0.966 [+0.634, +1.255] (n=11) | - | 0.00 | 0.22 | 0.00 |
| F_own | +1.085 [+0.856, +1.346] (n=11) | - | 0.00 | 0.27 | 0.00 |
| K_own | +0.429 [-0.083, +0.975] (n=11) | - | 0.33 | 0.18 | 0.00 |
| K_own_lag5 | +0.897 [+0.413, +1.341] (n=11) | - | 0.09 | 0.34 | 0.00 |
| K_own_x3 | -0.440 [-0.651, -0.186] (n=11) | - | 0.79 | 0.06 | 0.00 |
| K_pred | +1.601 [+1.036, +2.247] (n=11) | - | 0.04 | 0.47 | 0.00 |
| LK_own | +0.431 [-0.007, +0.871] (n=11) | - | 0.32 | 0.21 | 0.00 |
| LR1_nash | +0.333 [-0.143, +0.775] (n=11) | - | 0.36 | 0.10 | 0.00 |
| L_free | +1.141 [+0.880, +1.461] (n=11) | - | 0.00 | 0.37 | 0.00 |
| R1_nash | +0.455 [-0.024, +0.903] (n=11) | - | 0.27 | 0.11 | 0.00 |
| S1_cartel | +1.049 [+0.669, +1.428] (n=11) | - | 0.00 | 0.19 | 0.00 |

## Pre-registered decision rules


## Secondary

- **H6 R1_nash** I(rounds 2-30) R1_nash - F_own -0.607 [-1.033, -0.220], p = 0.016; keeps the forced Nash price in 27% of later rounds -> **SUPPORTED**

## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7a forced Nash vs sham (round 1)** R1_nash - S1_cartel -0.593 [-1.052, -0.169], p = 0.023; holds the forced price in 27% of later rounds -> **SUPPORTED**
- **sham vs F_own (round 1, descriptive)** S1_cartel - F_own -0.014 [-0.168, +0.114], p = 0.938; holds the forced price in 67% of later rounds
- **H7b own, real (R1_nash)** R1_nash - F_own -0.607 [-1.033, -0.220], p = 0.016; holds the forced price in 27% of later rounds -> **SUPPORTED**
- **H7b/H7c own, fake row (K_own)** K_own - F_own -0.632 [-1.054, -0.248], p = 0.023 -> **SUPPORTED**
- **H7b predecessor's, fake row (K_pred)** K_pred - F_own +0.522 [+0.011, +1.137], p = 0.160 -> **NOT SUPPORTED**
- **H7b competitor's, once (C1_nash)** C1_nash - F_own -0.123 [-0.267, -0.013], p = 0.109 -> **SUPPORTED**
- **H7e live: forced Nash round 1** LR1_nash - L_free -0.787 [-1.296, -0.315], p = 0.020; holds the forced price in 36% of later rounds; incumbent price shift +0.024 (control +0.035), market gain +0.49 (control +0.69) -> **SUPPORTED**
- **H7e live: fake row** LK_own - L_free -0.688 [-1.074, -0.336], p = 0.008; incumbent price shift +0.025 (control +0.035), market gain +0.54 (control +0.69) -> **SUPPORTED**

## Addendum 3

- **H8c recency: one fake row 5 rounds back vs F_own** K_own_lag5 - F_own -0.165 [-0.566, +0.116], p = 1.000 -> **NOT SUPPORTED**
- **H8c recency: 5 rounds back vs most recent** K_own_lag5 - K_own +0.467 [+0.129, +0.871], p = 0.031 -> **NOT SUPPORTED**
- **H8c dose: 3 fake rows vs 1** K_own_x3 - K_own -0.863 [-1.390, -0.386], p = 0.016 -> **SUPPORTED**

Excluded branches (>20% parse failures): 0
