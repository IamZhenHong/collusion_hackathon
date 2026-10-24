# gpt41mini_PIall__anthropic-claude-haiku-5p5-noreason

Bases: 20; branches: 200; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| C1_nash | +0.931 [+0.854, +1.003] (n=20) | - | 0.00 | 0.12 | 0.00 |
| F_own | +0.890 [+0.777, +0.992] (n=20) | - | 0.00 | 0.16 | 0.00 |
| K_own | +0.753 [+0.606, +0.882] (n=20) | - | 0.05 | 0.11 | 0.00 |
| R1_nash | +0.654 [+0.462, +0.823] (n=20) | - | 0.13 | 0.08 | 0.00 |
| S1_cartel | +0.937 [+0.859, +1.000] (n=20) | - | 0.00 | 0.03 | 0.00 |

## Pre-registered decision rules


## Secondary

- **H6 R1_nash** I(rounds 2-30) R1_nash - F_own -0.232 [-0.427, -0.063], p = 0.003; keeps the forced Nash price in 13% of later rounds -> **SUPPORTED**

## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7a forced Nash vs sham (round 1)** R1_nash - S1_cartel -0.283 [-0.490, -0.102], p = 0.008; holds the forced price in 13% of later rounds -> **SUPPORTED**
- **sham vs F_own (round 1, descriptive)** S1_cartel - F_own +0.051 [-0.016, +0.135], p = 0.642; holds the forced price in 62% of later rounds
- **H7b own, real (R1_nash)** R1_nash - F_own -0.232 [-0.427, -0.063], p = 0.003; holds the forced price in 13% of later rounds -> **SUPPORTED**
- **H7b/H7c own, fake row (K_own)** K_own - F_own -0.137 [-0.251, -0.045], p = 0.008 -> **SUPPORTED**
- **H7b competitor's, once (C1_nash)** C1_nash - F_own +0.044 [-0.010, +0.104], p = 0.152 -> **NOT SUPPORTED**

Excluded branches (>20% parse failures): 0
