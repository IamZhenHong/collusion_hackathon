# gpt41mini_PI_exp9__openai-gpt-4p1-mini

Bases: 10; branches: 100; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| F_own | +0.737 [+0.602, +0.879] (n=10) | - | 0.00 | 0.00 | 0.00 |
| K_own | -0.498 [-0.654, -0.287] (n=10) | - | 0.86 | 0.00 | 0.00 |
| K_own_br | +0.006 [+0.003, +0.009] (n=10) | - | 0.00 | 0.00 | 0.00 |
| K_own_cartel | +0.761 [+0.628, +0.893] (n=10) | - | 0.00 | 0.00 | 0.00 |
| K_own_cost | +0.769 [+0.619, +0.919] (n=10) | - | 0.00 | 0.00 | 0.00 |

## Pre-registered decision rules


## Secondary


## Addendum 2 (experiment 7), I over rounds 2-30 (11-30 for round 10)

- **H7b/H7c own, fake row (K_own)** K_own - F_own -1.233 [-1.499, -0.933], p = 0.002 -> **SUPPORTED**

## Addendum 4, test 1: copy or learn (I and newcomer profit per round, rounds 1-30)

- **H9a sham row (cartel price) vs F_own** I +0.024 [-0.037, +0.109] (rounds 1-5: +0.016 [-0.039, +0.077]); profit/round -0.54 [-2.00, +0.37] $; at the fake price: rounds 1-5 46%, rounds 21-30 40%
- **H9b profitable row (best response) vs F_own** I -0.731 [-0.876, -0.595] (rounds 1-5: -0.771 [-0.898, -0.653]); profit/round +9.90 [+7.50, +12.47] $; at the fake price: rounds 1-5 100%, rounds 21-30 100%
- **bad row (unit cost) vs F_own** I +0.032 [-0.010, +0.108] (rounds 1-5: -0.002 [-0.059, +0.063]); profit/round -0.57 [-1.96, +0.22] $; at the fake price: rounds 1-5 0%, rounds 21-30 0%
- **Nash row (reference) vs F_own** I -1.235 [-1.500, -0.935] (rounds 1-5: -1.260 [-1.518, -0.958]); profit/round +2.55 [+0.40, +4.87] $; at the fake price: rounds 1-5 86%, rounds 21-30 86%
- **H9c reading (bad row):** profit-sensitive (share at $1.00: 0% in rounds 1-5, 0% in 21-30)

Excluded branches (>20% parse failures): 0
