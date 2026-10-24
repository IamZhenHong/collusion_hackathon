# gpt41mini_PI_exp10__openai-gpt-4p1-mini

Bases: 10; branches: 100; metric I over post-branch rounds 1-30.
Intervals: 95% bootstrap over bases. p = paired Wilcoxon on base-level differences.

## Arms (inheritance index I, rounds 1-30; lift = I - I(F_hidden))

| arm | I | lift | below-Nash | overshoot-up | parse fail |
|---|---|---|---|---|---|
| F_own | +0.730 [+0.590, +0.877] (n=10) | - | 0.00 | 0.00 | 0.00 |
| K_br_low | +0.770 [+0.622, +0.919] (n=10) | - | 0.00 | 0.00 | 0.00 |
| K_own_br | +0.006 [+0.003, +0.009] (n=10) | - | 0.00 | 0.00 | 0.00 |
| K_up_high | +0.987 [+0.857, +1.112] (n=10) | - | 0.00 | 0.16 | 0.00 |
| K_up_true | +0.793 [+0.664, +0.925] (n=10) | - | 0.00 | 0.00 | 0.00 |

## Pre-registered decision rules


## Secondary


## Addendum 5: price vs displayed profit (I over rounds 1-30)

- **H10a same competitive price, low vs true profit** K_br_low - K_own_br +0.764 [+0.615, +0.914], p = 0.002; K_br_low at the fake price in 0% of rounds 1-5, 0% of 21-30 -> **SUPPORTED**
- **H10b same high price, high vs true profit** K_up_high - K_up_true +0.193 [+0.140, +0.267], p = 0.002; K_up_high at the fake price in 56% of rounds 1-5, 6% of 21-30 -> **SUPPORTED**
- **best-response row (true profit) vs F_own** K_own_br - F_own -0.724 [-0.872, -0.583], p = 0.002; K_own_br at the fake price in 100% of rounds 1-5, 100% of 21-30
- **best-response price, low profit vs F_own** K_br_low - F_own +0.040 [+0.000, +0.118], p = 0.500; K_br_low at the fake price in 0% of rounds 1-5, 0% of 21-30
- **above-cartel price, true profit vs F_own** K_up_true - F_own +0.063 [+0.003, +0.157], p = 0.062; K_up_true at the fake price in 0% of rounds 1-5, 0% of 21-30
- **above-cartel price, high profit vs F_own** K_up_high - F_own +0.256 [+0.165, +0.360], p = 0.002; K_up_high at the fake price in 56% of rounds 1-5, 6% of 21-30

Excluded branches (>20% parse failures): 0
