# gpt41mini_PC__qwen-qwen3-14b-deepinfra-nothink

Bases: 10; branches: 180; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| F_hidden | +1.027 [+1.017, +1.038] (n=10) | - | 0.00 | 0.20 | 0.00 |
| F_own | +0.768 [+0.645, +0.894] (n=10) | -0.259 [-0.378, -0.140] | 0.00 | 0.15 | 0.00 |
| F_placebo | +0.786 [+0.655, +0.914] (n=10) | -0.240 [-0.367, -0.120] | 0.00 | 0.10 | 0.00 |
| F_pred | +0.915 [+0.838, +0.979] (n=10) | -0.112 [-0.185, -0.053] | 0.00 | 0.16 | 0.00 |
| Fix_AC | +0.889 [+0.760, +0.994] (n=10) | -0.138 [-0.262, -0.038] | 0.00 | 0.20 | 0.00 |
| Fix_decision | +0.797 [+0.664, +0.925] (n=10) | -0.230 [-0.357, -0.109] | 0.00 | 0.15 | 0.00 |
| Fix_placebo | +0.791 [+0.656, +0.922] (n=10) | -0.236 [-0.365, -0.111] | 0.00 | 0.15 | 0.00 |
| Fix_system | +0.824 [+0.695, +0.945] (n=10) | -0.203 [-0.326, -0.089] | 0.00 | 0.20 | 0.00 |
| Fix_verdict | +0.780 [+0.624, +0.915] (n=10) | -0.247 [-0.397, -0.119] | 0.00 | 0.16 | 0.00 |

## Pre-registered decision rules

- **H1a** lift(F_own) -0.259 [-0.378, -0.140], lift(F_pred) -0.112 [-0.185, -0.053], ratio +2.31 [+1.66, +3.69]; I(F_own) - I(F_pred) -0.147 [-0.224, -0.066], p = 0.016 -> **NOT SUPPORTED**
- **H1b** lift(F_pred) -0.112 [-0.185, -0.053], p = 0.002 -> **NOT SUPPORTED**
- **H3** lift(F_own) -0.259 [-0.378, -0.140]; share of lift removed: Fix_decision +0.11 [+0.00, +0.34], Fix_system +0.22 [+0.05, +0.46]; I(Fix_system) - I(Fix_decision) +0.027 [+0.000, +0.055], p = 0.125; overshoot-up 0.15 / 0.20 -> **NOT EVALUABLE (lift(F_own) interval includes 0)**

## Secondary


Excluded branches (>20% parse failures): 0
