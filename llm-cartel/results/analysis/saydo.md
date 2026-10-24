# Say-do probe (H8e, descriptive)

682 statements; judges openai/gpt-4.1-mini vs anthropic/claude-haiku-5.5+noreason: raw agreement 83%, Cohen's kappa 0.72. Shares below use only agreed labels.

| set | newcomer | arm | n agreed | MATCH | LOWER | says LOWER, prices high (I>0.5) | says MATCH, prices low (I<=0.5) |
|---|---|---|---|---|---|---|---|
| gpt41mini_PI2 | openai-gpt-4p1-mini | C1_nash | 19/22 | 79% | 21% | 50% of LOWER | 0% of MATCH |
| gpt41mini_PI2 | openai-gpt-4p1-mini | F_own | 20/22 | 85% | 15% | 0% of LOWER | 6% of MATCH |
| gpt41mini_PI2 | openai-gpt-4p1-mini | K_own | 17/22 | 29% | 71% | 0% of LOWER | 40% of MATCH |
| gpt41mini_PI2 | openai-gpt-4p1-mini | K_own_lag5 | 20/22 | 60% | 40% | 0% of LOWER | 25% of MATCH |
| gpt41mini_PI2 | openai-gpt-4p1-mini | K_own_x3 | 16/22 | 19% | 81% | 0% of LOWER | 33% of MATCH |
| gpt41mini_PI2 | openai-gpt-4p1-mini | K_pred | 20/22 | 25% | 75% | 0% of LOWER | 20% of MATCH |
| gpt41mini_PI2 | openai-gpt-4p1-mini | LK_own | 19/22 | 37% | 63% | 8% of LOWER | 43% of MATCH |
| gpt41mini_PI2 | openai-gpt-4p1-mini | LR1_nash | 21/22 | 33% | 62% | 15% of LOWER | 43% of MATCH |
| gpt41mini_PI2 | openai-gpt-4p1-mini | L_free | 17/22 | 82% | 18% | 0% of LOWER | 0% of MATCH |
| gpt41mini_PI2 | openai-gpt-4p1-mini | R1_nash | 18/22 | 28% | 72% | 15% of LOWER | 40% of MATCH |
| gpt41mini_PI2 | openai-gpt-4p1-mini | S1_cartel | 19/22 | 100% | 0% | nan% of LOWER | 26% of MATCH |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | C1_nash | 10/22 | 0% | 80% | 75% of LOWER | nan% of MATCH |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | F_own | 14/22 | 0% | 57% | 88% of LOWER | nan% of MATCH |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | K_own | 19/22 | 5% | 89% | 47% of LOWER | 0% of MATCH |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | K_own_lag5 | 15/22 | 0% | 93% | 71% of LOWER | nan% of MATCH |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | K_own_x3 | 20/22 | 0% | 100% | 5% of LOWER | nan% of MATCH |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | K_pred | 20/22 | 0% | 90% | 94% of LOWER | nan% of MATCH |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | LK_own | 17/22 | 12% | 82% | 50% of LOWER | 0% of MATCH |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | LR1_nash | 14/22 | 0% | 79% | 45% of LOWER | nan% of MATCH |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | L_free | 17/22 | 0% | 71% | 92% of LOWER | nan% of MATCH |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | R1_nash | 13/22 | 0% | 92% | 50% of LOWER | nan% of MATCH |
| gpt41mini_PI2 | qwen-qwen3-14b-deepinfra-nothink | S1_cartel | 15/22 | 0% | 73% | 82% of LOWER | nan% of MATCH |
| gpt41mini_PIall | anthropic-claude-haiku-5p5-noreason | C1_nash | 38/40 | 84% | 16% | 100% of LOWER | 3% of MATCH |
| gpt41mini_PIall | anthropic-claude-haiku-5p5-noreason | F_own | 39/40 | 59% | 18% | 43% of LOWER | 4% of MATCH |
| gpt41mini_PIall | anthropic-claude-haiku-5p5-noreason | K_own | 32/39 | 72% | 22% | 43% of LOWER | 13% of MATCH |
| gpt41mini_PIall | anthropic-claude-haiku-5p5-noreason | R1_nash | 37/40 | 35% | 62% | 61% of LOWER | 23% of MATCH |
| gpt41mini_PIall | anthropic-claude-haiku-5p5-noreason | S1_cartel | 38/39 | 66% | 18% | 71% of LOWER | 0% of MATCH |
