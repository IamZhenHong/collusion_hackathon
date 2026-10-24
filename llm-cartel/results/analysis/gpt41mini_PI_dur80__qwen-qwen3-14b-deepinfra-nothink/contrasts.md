# gpt41mini_PI_dur80__qwen-qwen3-14b-deepinfra-nothink

Bases: 9; branches: 54; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| F_own | +0.857 [+0.711, +0.987] (n=9) | - | 0.00 | 0.02 | 0.00 |
| K_own | +0.528 [+0.073, +0.906] (n=9) | - | 0.22 | 0.04 | 0.00 |
| R1_nash | +0.544 [+0.104, +0.909] (n=9) | - | 0.26 | 0.04 | 0.00 |

## Pre-registered decision rules


## Secondary

- **H6 R1_nash** I(rounds 2-30) R1_nash - F_own -0.359 [-0.759, -0.042], p = 0.156; keeps the forced Nash price in 26% of later rounds -> **SUPPORTED**

## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7b own, real (R1_nash)** R1_nash - F_own -0.359 [-0.759, -0.042], p = 0.156; holds the forced price in 26% of later rounds -> **SUPPORTED**
- **H7b/H7c own, fake row (K_own)** K_own - F_own -0.307 [-0.709, +0.002], p = 0.578 -> **NOT SUPPORTED**

## Addendum 3

- **H8b durability: fake row vs F_own, rounds 61-80** K_own - F_own -0.269 [-0.643, +0.010], p = 0.438; rounds 61-80 at the Nash price: K_own 21%, F_own 0% -> **NOT SUPPORTED**
- **H8b durability: forced round vs F_own, rounds 61-80** R1_nash - F_own -0.420 [-0.819, -0.092], p = 0.094; rounds 61-80 at the Nash price: R1_nash 32%, F_own 0% -> **SUPPORTED**

Excluded branches (>20% parse failures): 0
