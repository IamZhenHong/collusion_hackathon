# gpt41mini_PI_exp8__qwen-qwen3-14b-deepinfra-nothink

Bases: 9; branches: 72; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| F_own | +0.857 [+0.710, +0.987] (n=9) | - | 0.00 | 0.05 | 0.00 |
| K_own | +0.531 [+0.079, +0.906] (n=9) | - | 0.22 | 0.09 | 0.00 |
| K_own_lag5 | +0.718 [+0.344, +0.976] (n=9) | - | 0.11 | 0.05 | 0.00 |
| K_own_x3 | -0.443 [-0.614, -0.138] (n=9) | - | 0.90 | 0.00 | 0.00 |

## Pre-registered decision rules


## Secondary


## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7b/H7c own, fake row (K_own)** K_own - F_own -0.318 [-0.745, +0.009], p = 0.688 -> **NOT SUPPORTED**

## Addendum 3

- **H8c recency: one fake row 5 rounds back vs F_own** K_own_lag5 - F_own -0.143 [-0.555, +0.118], p = 1.000 -> **NOT SUPPORTED**
- **H8c recency: 5 rounds back vs most recent** K_own_lag5 - K_own +0.176 [-0.016, +0.540], p = 1.000 -> **NOT SUPPORTED**
- **H8c dose: 3 fake rows vs 1** K_own_x3 - K_own -0.975 [-1.398, -0.521], p = 0.016 -> **SUPPORTED**

Excluded branches (>20% parse failures): 0
