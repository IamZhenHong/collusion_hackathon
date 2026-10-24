# gpt41mini_PI_exp8__openai-gpt-4p1-mini

Bases: 9; branches: 72; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| F_own | +0.693 [+0.571, +0.820] (n=9) | - | 0.00 | 0.00 | 0.00 |
| K_own | -0.435 [-0.631, -0.166] (n=9) | - | 0.78 | 0.00 | 0.00 |
| K_own_lag5 | +0.042 [-0.345, +0.431] (n=9) | - | 0.45 | 0.00 | 0.00 |
| K_own_x3 | -0.566 [-0.636, -0.453] (n=9) | - | 0.89 | 0.00 | 0.00 |

## Pre-registered decision rules


## Secondary


## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7b/H7c own, fake row (K_own)** K_own - F_own -1.126 [-1.411, -0.779], p = 0.008 -> **SUPPORTED**

## Addendum 3

- **H8c recency: one fake row 5 rounds back vs F_own** K_own_lag5 - F_own -0.654 [-1.113, -0.217], p = 0.031 -> **SUPPORTED**
- **H8c recency: 5 rounds back vs most recent** K_own_lag5 - K_own +0.472 [+0.076, +0.886], p = 0.094 -> **NOT SUPPORTED**
- **H8c dose: 3 fake rows vs 1** K_own_x3 - K_own -0.130 [-0.317, -0.003], p = 0.250 -> **SUPPORTED**

Excluded branches (>20% parse failures): 0
