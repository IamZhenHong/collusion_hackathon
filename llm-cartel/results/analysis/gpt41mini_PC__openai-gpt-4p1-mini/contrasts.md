# gpt41mini_PC__openai-gpt-4p1-mini

Bases: 10; branches: 180; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| F_hidden | +0.800 [+0.687, +0.915] (n=10) | - | 0.00 | 0.02 | 0.00 |
| F_own | +0.443 [+0.281, +0.619] (n=10) | -0.357 [-0.530, -0.183] | 0.00 | 0.00 | 0.00 |
| F_placebo | +0.371 [+0.182, +0.576] (n=10) | -0.430 [-0.630, -0.229] | 0.00 | 0.00 | 0.00 |
| F_pred | +0.426 [+0.266, +0.611] (n=10) | -0.375 [-0.575, -0.181] | 0.00 | 0.00 | 0.00 |
| Fix_AC | +0.458 [+0.285, +0.645] (n=10) | -0.342 [-0.513, -0.175] | 0.00 | 0.00 | 0.00 |
| Fix_decision | +0.395 [+0.228, +0.588] (n=10) | -0.405 [-0.595, -0.215] | 0.00 | 0.00 | 0.00 |
| Fix_placebo | +0.445 [+0.287, +0.622] (n=10) | -0.356 [-0.555, -0.167] | 0.00 | 0.00 | 0.00 |
| Fix_system | +0.472 [+0.316, +0.640] (n=10) | -0.329 [-0.506, -0.167] | 0.00 | 0.00 | 0.00 |
| Fix_verdict | +0.231 [+0.164, +0.305] (n=10) | -0.569 [-0.692, -0.439] | 0.00 | 0.00 | 0.00 |

## Pre-registered decision rules

- **H1a** lift(F_own) -0.357 [-0.530, -0.183], lift(F_pred) -0.375 [-0.575, -0.181], ratio +0.95 [+0.77, +1.27]; I(F_own) - I(F_pred) +0.018 [-0.072, +0.097], p = 0.844 -> **NOT SUPPORTED**
- **H1b** lift(F_pred) -0.375 [-0.575, -0.181], p = 0.010 -> **NOT SUPPORTED**
- **H3** lift(F_own) -0.357 [-0.530, -0.183]; share of lift removed: Fix_decision -0.13 [-0.47, +0.11], Fix_system +0.08 [-0.12, +0.27]; I(Fix_system) - I(Fix_decision) +0.077 [-0.020, +0.204], p = 0.625; overshoot-up 0.00 / 0.00 -> **NOT EVALUABLE (lift(F_own) interval includes 0)**

## Secondary


Excluded branches (>20% parse failures): 0
