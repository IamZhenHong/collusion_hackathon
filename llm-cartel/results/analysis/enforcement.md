# Enforcement audit (addendum 4, test 3; existing live-incumbent branches)

Incumbent move = its mean price over the 5 rounds after the newcomer's deviation minus its price in the
deviation round; benchmark = moving to its static best response to the newcomer's deviation price.

| set | newcomer | arm | branches | with a deviation | incumbent move | competitive benchmark | response ratio | incumbent cut > $0.05 |
|---|---|---|---|---|---|---|---|---|
| gpt41mini_PI | openai-gpt-4p1-mini | L_hidden | 18 | 18 | -0.027 | -0.710 | 0.00 (median) | 11% |
| gpt41mini_PI | openai-gpt-4p1-mini | L_own | 18 | 18 | +0.001 | -0.676 | 0.00 (median) | 6% |
| gpt41mini_PI | qwen-qwen3-14b-deepinfra-nothink | L_hidden | 18 | 18 | -0.013 | -0.701 | 0.00 (median) | 11% |
| gpt41mini_PI | qwen-qwen3-14b-deepinfra-nothink | L_own | 18 | 18 | -0.044 | -0.769 | 0.00 (median) | 6% |
| gpt41mini_PI2 | openai-gpt-4p1-mini | LK_own | 22 | 14 | +0.011 | -0.633 | 0.00 (median) | 0% |
| gpt41mini_PI2 | openai-gpt-4p1-mini | LR1_nash | 22 | 22 | +0.005 | -0.587 | 0.00 (median) | 0% |
| gpt41mini_PI2 | openai-gpt-4p1-mini | L_free | 22 | 4 | +0.005 | -0.794 | -0.01 (median) | 0% |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | LK_own | 22 | 10 | +0.038 | -0.666 | 0.00 (median) | 0% |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | LR1_nash | 22 | 22 | +0.016 | -0.587 | 0.00 (median) | 0% |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | L_free | 22 | 1 | +0.000 | -1.010 | 0.00 (median) | 0% |
| gpt41mini_PI_exp7 | openai-gpt-4p1-mini | LK_own | 18 | 14 | -0.017 | -0.663 | 0.00 (median) | 21% |
| gpt41mini_PI_exp7 | openai-gpt-4p1-mini | LR1_nash | 18 | 18 | -0.013 | -0.687 | 0.00 (median) | 17% |
| gpt41mini_PI_exp7 | openai-gpt-4p1-mini | L_free | 18 | 0 | - | - | - | - |
| gpt41mini_PI_exp7 | qwen-qwen3-14b-deepinfra-nothink | LK_own | 18 | 4 | +0.000 | -0.653 | 0.00 (median) | 0% |
| gpt41mini_PI_exp7 | qwen-qwen3-14b-deepinfra-nothink | LR1_nash | 18 | 18 | +0.019 | -0.682 | 0.00 (median) | 0% |
| gpt41mini_PI_exp7 | qwen-qwen3-14b-deepinfra-nothink | L_free | 18 | 0 | - | - | - | - |

Newcomer's cumulative profit over 30 rounds minus the same base's L_free (mean of seeds), in dollars:

- gpt41mini_PI2 / openai-gpt-4p1-mini / LR1_nash: +38.7 [-37.2, +104.6] (n = 11 bases)
- gpt41mini_PI2 / openai-gpt-4p1-mini / LK_own: +30.4 [-34.2, +82.2] (n = 11 bases)
- gpt41mini_PI2 / qwen-qwen3-14b-deepinfra-nothink / LR1_nash: +130.8 [+44.2, +241.2] (n = 11 bases)
- gpt41mini_PI2 / qwen-qwen3-14b-deepinfra-nothink / LK_own: +126.6 [+35.2, +234.3] (n = 11 bases)
- gpt41mini_PI_exp7 / openai-gpt-4p1-mini / LR1_nash: +83.8 [+18.1, +146.0] (n = 9 bases)
- gpt41mini_PI_exp7 / openai-gpt-4p1-mini / LK_own: +99.5 [+35.3, +163.3] (n = 9 bases)
- gpt41mini_PI_exp7 / qwen-qwen3-14b-deepinfra-nothink / LR1_nash: +18.3 [+4.2, +42.5] (n = 9 bases)
- gpt41mini_PI_exp7 / qwen-qwen3-14b-deepinfra-nothink / LK_own: +10.8 [+0.3, +29.1] (n = 9 bases)
