# gpt41mini_PI_exp6__qwen-qwen3-14b-deepinfra-nothink

Bases: 9; branches: 90; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| F_hidden | +1.110 [+1.081, +1.134] (n=9) | - | 0.00 | 0.06 | 0.00 |
| F_own | +0.858 [+0.711, +0.987] (n=9) | -0.252 [-0.376, -0.142] | 0.00 | 0.05 | 0.00 |
| R10_nash | +0.512 [+0.194, +0.807] (n=9) | -0.598 [-0.922, -0.306] | 0.23 | 0.04 | 0.00 |
| R1_nash | +0.544 [+0.104, +0.908] (n=9) | -0.566 [-1.012, -0.204] | 0.22 | 0.09 | 0.00 |
| R1_nash_hidden | +1.061 [+1.052, +1.069] (n=9) | -0.049 [-0.065, -0.028] | 0.00 | 0.03 | 0.00 |

## Pre-registered decision rules


## Secondary

- **H6 R1_nash** I(rounds 2-30) R1_nash - F_own -0.307 [-0.732, +0.010], p = 0.625; keeps the forced Nash price in 22% of later rounds -> **NOT SUPPORTED**
- **H6 R10_nash** I(rounds 11-30) R10_nash - F_own -0.503 [-1.009, -0.130], p = 0.188; keeps the forced Nash price in 33% of later rounds -> **SUPPORTED**
- **H6 R1_nash_hidden** I(rounds 2-30) R1_nash_hidden - F_hidden +0.008 [+0.000, +0.021], p = 0.500; keeps the forced Nash price in 0% of later rounds -> **NOT SUPPORTED**

## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7b own, real (R1_nash)** R1_nash - F_own -0.307 [-0.732, +0.010], p = 0.625; holds the forced price in 22% of later rounds -> **NOT SUPPORTED**

Excluded branches (>20% parse failures): 0
