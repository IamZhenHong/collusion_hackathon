# gpt41mini_PI_exp9fork__openai-gpt-4p1-mini

Bases: 10; branches: 60; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| fork_deladj | -0.530 [-0.656, -0.363] (n=10) | - | 0.87 | 0.00 | 0.03 |
| fork_delfake | -0.526 [-0.656, -0.352] (n=10) | - | 0.86 | 0.00 | 0.03 |
| fork_keep | -0.530 [-0.656, -0.363] (n=10) | - | 0.87 | 0.00 | 0.03 |

## Pre-registered decision rules


## Secondary


## Addendum 4, test 2: does the effect outlast the row? (I over rounds 11-35, after the fork)

- **fork_delfake - fork_keep** +0.017 [+0.000, +0.050], p = 1.000
- **fork_deladj - fork_keep** +0.000 [+0.000, +0.000], p = nan
- **fork_delfake - fork_deladj** +0.017 [+0.000, +0.050], p = 1.000
  - fork_keep: I(rounds 11-35) = -0.541 [-0.656, -0.386]
  - fork_delfake: I(rounds 11-35) = -0.524 [-0.656, -0.350]
  - fork_deladj: I(rounds 11-35) = -0.541 [-0.656, -0.386]

Excluded branches (>20% parse failures): 0
