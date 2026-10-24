# gpt41mini_PI2__openai-gpt-4p1-mini

Bases: 11; branches: 242; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| C1_nash | +0.792 [+0.506, +1.007] (n=11) | - | 0.00 | 0.18 | 0.00 |
| F_own | +0.736 [+0.419, +1.000] (n=11) | - | 0.00 | 0.18 | 0.00 |
| K_own | -0.028 [-0.419, +0.381] (n=11) | - | 0.54 | 0.01 | 0.00 |
| K_own_lag5 | +0.170 [-0.237, +0.571] (n=11) | - | 0.46 | 0.08 | 0.00 |
| K_own_x3 | -0.414 [-0.668, -0.067] (n=11) | - | 0.82 | 0.00 | 0.00 |
| K_pred | -0.258 [-0.602, +0.136] (n=11) | - | 0.64 | 0.00 | 0.00 |
| LK_own | -0.106 [-0.490, +0.299] (n=11) | - | 0.62 | 0.01 | 0.00 |
| LR1_nash | +0.003 [-0.416, +0.433] (n=11) | - | 0.55 | 0.01 | 0.00 |
| L_free | +0.754 [+0.438, +1.015] (n=11) | - | 0.00 | 0.25 | 0.00 |
| R1_nash | -0.074 [-0.464, +0.343] (n=11) | - | 0.59 | 0.01 | 0.00 |
| S1_cartel | +0.737 [+0.422, +1.001] (n=11) | - | 0.00 | 0.19 | 0.00 |

## Pre-registered decision rules


## Secondary

- **H6 R1_nash** I(rounds 2-30) R1_nash - F_own -0.808 [-1.238, -0.395], p = 0.008; keeps the forced Nash price in 59% of later rounds -> **SUPPORTED**

## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7a forced Nash vs sham (round 1)** R1_nash - S1_cartel -0.811 [-1.242, -0.395], p = 0.008; holds the forced price in 59% of later rounds -> **SUPPORTED**
- **sham vs F_own (round 1, descriptive)** S1_cartel - F_own +0.003 [-0.010, +0.020], p = 1.000; holds the forced price in 19% of later rounds
- **H7b own, real (R1_nash)** R1_nash - F_own -0.808 [-1.238, -0.395], p = 0.008; holds the forced price in 59% of later rounds -> **SUPPORTED**
- **H7b/H7c own, fake row (K_own)** K_own - F_own -0.770 [-1.202, -0.375], p = 0.002 -> **SUPPORTED**
- **H7b predecessor's, fake row (K_pred)** K_pred - F_own -0.995 [-1.425, -0.549], p = 0.002 -> **SUPPORTED**
- **H7b competitor's, once (C1_nash)** C1_nash - F_own +0.059 [-0.014, +0.177], p = 0.438 -> **NOT SUPPORTED**
- **H7e live: forced Nash round 1** LR1_nash - L_free -0.750 [-1.207, -0.331], p = 0.008; holds the forced price in 55% of later rounds; incumbent price shift +0.009 (control +0.014), market gain +0.47 (control +0.82) -> **SUPPORTED**
- **H7e live: fake row** LK_own - L_free -0.867 [-1.300, -0.444], p = 0.004; incumbent price shift +0.008 (control +0.014), market gain +0.41 (control +0.82) -> **SUPPORTED**

## Addendum 3

- **H8c recency: one fake row 5 rounds back vs F_own** K_own_lag5 - F_own -0.572 [-0.997, -0.202], p = 0.008 -> **SUPPORTED**
- **H8c recency: 5 rounds back vs most recent** K_own_lag5 - K_own +0.198 [+0.065, +0.348], p = 0.031 -> **NOT SUPPORTED**
- **H8c dose: 3 fake rows vs 1** K_own_x3 - K_own -0.382 [-0.784, -0.007], p = 0.094 -> **SUPPORTED**

Excluded branches (>20% parse failures): 0
