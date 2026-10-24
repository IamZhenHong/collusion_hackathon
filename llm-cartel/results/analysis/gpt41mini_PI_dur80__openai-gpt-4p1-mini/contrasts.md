# gpt41mini_PI_dur80__openai-gpt-4p1-mini

Bases: 9; branches: 54; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| F_own | +0.728 [+0.583, +0.874] (n=9) | - | 0.00 | 0.00 | 0.00 |
| K_own | -0.365 [-0.625, -0.095] (n=9) | - | 0.76 | 0.00 | 0.00 |
| R1_nash | -0.354 [-0.625, +0.011] (n=9) | - | 0.72 | 0.00 | 0.00 |

## Pre-registered decision rules


## Secondary

- **H6 R1_nash** I(rounds 2-30) R1_nash - F_own -1.083 [-1.447, -0.654], p = 0.016; keeps the forced Nash price in 72% of later rounds -> **SUPPORTED**

## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7b own, real (R1_nash)** R1_nash - F_own -1.083 [-1.447, -0.654], p = 0.016; holds the forced price in 72% of later rounds -> **SUPPORTED**
- **H7b/H7c own, fake row (K_own)** K_own - F_own -1.132 [-1.442, -0.766], p = 0.008 -> **SUPPORTED**

## Addendum 3

- **H8b durability: fake row vs F_own, rounds 61-80** K_own - F_own -1.148 [-1.445, -0.786], p = 0.008; rounds 61-80 at the Nash price: K_own 78%, F_own 0% -> **SUPPORTED**
- **H8b durability: forced round vs F_own, rounds 61-80** R1_nash - F_own -1.078 [-1.440, -0.652], p = 0.016; rounds 61-80 at the Nash price: R1_nash 72%, F_own 0% -> **SUPPORTED**

Excluded branches (>20% parse failures): 0
