# gpt41mini_PI_exp6__openai-gpt-4p1-mini

Bases: 9; branches: 90; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| F_hidden | +0.966 [+0.916, +1.014] (n=9) | - | 0.00 | 0.03 | 0.00 |
| F_own | +0.728 [+0.583, +0.874] (n=9) | -0.238 [-0.392, -0.080] | 0.00 | 0.00 | 0.00 |
| R10_nash | +0.260 [+0.030, +0.492] (n=9) | -0.706 [-0.932, -0.474] | 0.27 | 0.00 | 0.00 |
| R1_nash | -0.236 [-0.523, +0.118] (n=9) | -1.202 [-1.486, -0.866] | 0.62 | 0.00 | 0.00 |
| R1_nash_hidden | -0.012 [-0.093, +0.072] (n=9) | -0.978 [-1.076, -0.886] | 0.01 | 0.00 | 0.00 |

## Pre-registered decision rules


## Secondary

- **H6 R1_nash** I(rounds 2-30) R1_nash - F_own -0.964 [-1.343, -0.554], p = 0.008; keeps the forced Nash price in 62% of later rounds -> **SUPPORTED**
- **H6 R10_nash** I(rounds 11-30) R10_nash - F_own -0.655 [-1.138, -0.228], p = 0.062; keeps the forced Nash price in 39% of later rounds -> **SUPPORTED**
- **H6 R1_nash_hidden** I(rounds 2-30) R1_nash_hidden - F_hidden -0.946 [-1.036, -0.861], p = 0.004; keeps the forced Nash price in 1% of later rounds -> **SUPPORTED**

## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7b own, real (R1_nash)** R1_nash - F_own -0.964 [-1.343, -0.554], p = 0.008; holds the forced price in 62% of later rounds -> **SUPPORTED**

Excluded branches (>20% parse failures): 0
