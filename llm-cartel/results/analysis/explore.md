# Exploratory: the newcomer's held price (post-hoc; see analysis/explore.py)

## gpt41mini_PC / openai-gpt-4p1-mini

Share of branches by held price. All bases | only the 7 bases where the predecessor's last price differs from p_c.

| arm | n | competitor | pred_last | pred_earlier | best_resp | other | asym: competitor | asym: pred_last | asym: pred_earlier |
|---|---|---|---|---|---|---|---|---|---|
| F_hidden | 20 | 0.65 | 0.00 | 0.25 | 0.05 | 0.05 | 0.71 | 0.00 | 0.14 |
| F_own | 20 | 0.10 | 0.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| F_placebo | 20 | 0.10 | 0.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| F_pred | 20 | 0.10 | 0.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| Fix_AC | 20 | 0.10 | 0.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| Fix_decision | 20 | 0.10 | 0.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| Fix_placebo | 20 | 0.10 | 0.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| Fix_system | 20 | 0.10 | 0.00 | 0.90 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| Fix_verdict | 20 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |

## gpt41mini_PC / qwen-qwen3-14b-deepinfra-nothink

Share of branches by held price. All bases | only the 7 bases where the predecessor's last price differs from p_c.

| arm | n | competitor | pred_last | pred_earlier | best_resp | other | asym: competitor | asym: pred_last | asym: pred_earlier |
|---|---|---|---|---|---|---|---|---|---|
| F_hidden | 20 | 0.85 | 0.00 | 0.00 | 0.00 | 0.15 | 0.93 | 0.00 | 0.00 |
| F_own | 20 | 0.10 | 0.00 | 0.65 | 0.00 | 0.25 | 0.00 | 0.00 | 0.64 |
| F_placebo | 20 | 0.25 | 0.00 | 0.55 | 0.00 | 0.20 | 0.21 | 0.00 | 0.50 |
| F_pred | 20 | 0.45 | 0.05 | 0.30 | 0.00 | 0.20 | 0.36 | 0.07 | 0.29 |
| Fix_AC | 20 | 0.40 | 0.00 | 0.40 | 0.00 | 0.20 | 0.29 | 0.00 | 0.43 |
| Fix_decision | 20 | 0.20 | 0.00 | 0.55 | 0.00 | 0.25 | 0.14 | 0.00 | 0.50 |
| Fix_placebo | 20 | 0.20 | 0.00 | 0.55 | 0.00 | 0.25 | 0.14 | 0.00 | 0.50 |
| Fix_system | 20 | 0.20 | 0.00 | 0.55 | 0.00 | 0.25 | 0.14 | 0.00 | 0.50 |
| Fix_verdict | 20 | 0.20 | 0.00 | 0.50 | 0.00 | 0.30 | 0.14 | 0.00 | 0.50 |

## gpt41mini_PI / openai-gpt-4p1-mini

Share of branches by held price. All bases | only the 2 bases where the predecessor's last price differs from p_c.

| arm | n | competitor | pred_last | pred_earlier | best_resp | other | asym: competitor | asym: pred_last | asym: pred_earlier |
|---|---|---|---|---|---|---|---|---|---|
| F_hidden | 18 | 0.89 | 0.00 | 0.06 | 0.00 | 0.06 | 1.00 | 0.00 | 0.00 |
| F_own | 18 | 0.33 | 0.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| F_placebo | 18 | 0.33 | 0.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| F_pred | 18 | 0.33 | 0.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| Fix_AC | 18 | 0.28 | 0.00 | 0.72 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| Fix_decision | 18 | 0.33 | 0.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| Fix_placebo | 18 | 0.28 | 0.00 | 0.72 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| Fix_system | 18 | 0.33 | 0.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| Fix_verdict | 18 | 0.00 | 0.00 | 0.89 | 0.00 | 0.11 | 0.00 | 0.00 | 1.00 |
| L_hidden | 18 | 0.17 | 0.06 | 0.17 | 0.00 | 0.61 | 0.00 | 0.25 | 0.00 |
| L_own | 18 | 0.00 | 0.00 | 0.56 | 0.00 | 0.44 | 0.00 | 0.00 | 0.75 |
| M_authority | 18 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| M_authority_fresh | 18 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| M_authority_indep | 18 | 0.17 | 0.00 | 0.83 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| M_peer | 18 | 0.83 | 0.00 | 0.17 | 0.00 | 0.00 | 0.75 | 0.00 | 0.25 |
| M_peer_fresh | 18 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| N_mistake | 18 | 0.11 | 0.06 | 0.22 | 0.00 | 0.61 | 0.25 | 0.25 | 0.50 |
| N_other | 18 | 0.78 | 0.00 | 0.06 | 0.00 | 0.17 | 0.75 | 0.00 | 0.25 |
| N_own | 18 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |

Live arms (forced Nash price at round 10):

- L_hidden: I over rounds 1-9 = +0.965; keeps the forced Nash price in 54% of rounds 11-30 (8/18 branches hold it throughout)
- L_own: I over rounds 1-9 = +0.732; keeps the forced Nash price in 44% of rounds 11-30 (7/18 branches hold it throughout)
- F_own (replayed incumbent), same rounds 1-9: I = +0.708

## gpt41mini_PI / qwen-qwen3-14b-deepinfra-nothink

Share of branches by held price. All bases | only the 2 bases where the predecessor's last price differs from p_c.

| arm | n | competitor | pred_last | pred_earlier | best_resp | other | asym: competitor | asym: pred_last | asym: pred_earlier |
|---|---|---|---|---|---|---|---|---|---|
| F_hidden | 18 | 0.94 | 0.00 | 0.00 | 0.00 | 0.06 | 1.00 | 0.00 | 0.00 |
| F_own | 18 | 0.50 | 0.06 | 0.44 | 0.00 | 0.00 | 0.75 | 0.25 | 0.00 |
| F_placebo | 18 | 0.44 | 0.11 | 0.44 | 0.00 | 0.00 | 0.50 | 0.50 | 0.00 |
| F_pred | 18 | 0.67 | 0.00 | 0.22 | 0.00 | 0.11 | 1.00 | 0.00 | 0.00 |
| Fix_AC | 18 | 0.61 | 0.06 | 0.33 | 0.00 | 0.00 | 0.75 | 0.25 | 0.00 |
| Fix_decision | 18 | 0.44 | 0.11 | 0.44 | 0.00 | 0.00 | 0.50 | 0.50 | 0.00 |
| Fix_placebo | 18 | 0.50 | 0.06 | 0.44 | 0.00 | 0.00 | 0.75 | 0.25 | 0.00 |
| Fix_system | 18 | 0.44 | 0.11 | 0.44 | 0.00 | 0.00 | 0.50 | 0.50 | 0.00 |
| Fix_verdict | 18 | 0.39 | 0.11 | 0.33 | 0.00 | 0.17 | 0.00 | 0.50 | 0.50 |
| L_hidden | 18 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| L_own | 18 | 0.22 | 0.17 | 0.33 | 0.00 | 0.28 | 0.00 | 0.75 | 0.00 |
| M_authority | 18 | 0.89 | 0.00 | 0.11 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| M_authority_fresh | 18 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| M_authority_indep | 18 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| M_peer | 18 | 0.89 | 0.00 | 0.11 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| M_peer_fresh | 18 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| N_mistake | 18 | 0.39 | 0.00 | 0.00 | 0.00 | 0.61 | 0.00 | 0.00 | 0.00 |
| N_other | 18 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| N_own | 18 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |

Live arms (forced Nash price at round 10):

- L_hidden: I over rounds 1-9 = +1.864; keeps the forced Nash price in 98% of rounds 11-30 (17/18 branches hold it throughout)
- L_own: I over rounds 1-9 = +0.891; keeps the forced Nash price in 28% of rounds 11-30 (5/18 branches hold it throughout)
- F_own (replayed incumbent), same rounds 1-9: I = +0.891

## gpt41mini_PI_exp6 / openai-gpt-4p1-mini

Share of branches by held price. All bases | only the 2 bases where the predecessor's last price differs from p_c.

| arm | n | competitor | pred_last | pred_earlier | best_resp | other | asym: competitor | asym: pred_last | asym: pred_earlier |
|---|---|---|---|---|---|---|---|---|---|
| F_hidden | 18 | 0.72 | 0.00 | 0.11 | 0.00 | 0.17 | 0.75 | 0.00 | 0.25 |
| F_own | 18 | 0.33 | 0.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| R10_nash | 18 | 0.00 | 0.00 | 0.61 | 0.00 | 0.39 | 0.00 | 0.00 | 1.00 |
| R1_nash | 18 | 0.00 | 0.00 | 0.39 | 0.00 | 0.61 | 0.00 | 0.00 | 0.25 |
| R1_nash_hidden | 18 | 0.00 | 0.00 | 0.06 | 0.22 | 0.72 | 0.00 | 0.00 | 0.00 |

Live arms (forced Nash price at round 10):

- R10_nash: I over rounds 1-9 = +0.677; keeps the forced Nash price in 39% of rounds 11-30 (7/18 branches hold it throughout)
- R1_nash: I over rounds 1-9 = +nan; keeps the forced Nash price in 62% of rounds 11-30 (11/18 branches hold it throughout)
- R1_nash_hidden: I over rounds 1-9 = +nan; keeps the forced Nash price in 1% of rounds 11-30 (0/18 branches hold it throughout)
- F_own (replayed incumbent), same rounds 1-9: I = +0.728

## gpt41mini_PI_exp6 / qwen-qwen3-14b-deepinfra-nothink

Share of branches by held price. All bases | only the 2 bases where the predecessor's last price differs from p_c.

| arm | n | competitor | pred_last | pred_earlier | best_resp | other | asym: competitor | asym: pred_last | asym: pred_earlier |
|---|---|---|---|---|---|---|---|---|---|
| F_hidden | 18 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| F_own | 18 | 0.50 | 0.06 | 0.44 | 0.00 | 0.00 | 0.75 | 0.25 | 0.00 |
| R10_nash | 18 | 0.33 | 0.00 | 0.33 | 0.00 | 0.33 | 1.00 | 0.00 | 0.00 |
| R1_nash | 18 | 0.28 | 0.17 | 0.33 | 0.00 | 0.22 | 0.25 | 0.75 | 0.00 |
| R1_nash_hidden | 18 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |

Live arms (forced Nash price at round 10):

- R10_nash: I over rounds 1-9 = +0.891; keeps the forced Nash price in 33% of rounds 11-30 (6/18 branches hold it throughout)
- R1_nash: I over rounds 1-9 = +nan; keeps the forced Nash price in 22% of rounds 11-30 (4/18 branches hold it throughout)
- R1_nash_hidden: I over rounds 1-9 = +nan; keeps the forced Nash price in 0% of rounds 11-30 (0/18 branches hold it throughout)
- F_own (replayed incumbent), same rounds 1-9: I = +0.891

## gpt41mini_PI_exp7 / openai-gpt-4p1-mini

Share of branches by held price. All bases | only the 2 bases where the predecessor's last price differs from p_c.

| arm | n | competitor | pred_last | pred_earlier | best_resp | other | asym: competitor | asym: pred_last | asym: pred_earlier |
|---|---|---|---|---|---|---|---|---|---|
| C1_nash | 18 | 0.22 | 0.00 | 0.78 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| F_own | 18 | 0.33 | 0.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| F_pred | 18 | 0.33 | 0.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| Fix_system | 18 | 0.33 | 0.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| ID_system | 18 | 0.11 | 0.00 | 0.89 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| K_own | 18 | 0.00 | 0.00 | 0.17 | 0.00 | 0.83 | 0.00 | 0.00 | 0.00 |
| K_pred | 18 | 0.00 | 0.00 | 0.11 | 0.00 | 0.89 | 0.00 | 0.00 | 0.00 |
| LK_own | 18 | 0.00 | 0.00 | 0.28 | 0.00 | 0.72 | 0.00 | 0.00 | 0.00 |
| LR1_nash | 18 | 0.00 | 0.00 | 0.39 | 0.00 | 0.61 | 0.00 | 0.00 | 0.00 |
| L_free | 18 | 0.33 | 0.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| R10_nash | 18 | 0.00 | 0.00 | 0.56 | 0.00 | 0.44 | 0.00 | 0.00 | 1.00 |
| R1_br | 18 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| R1_nash | 18 | 0.00 | 0.00 | 0.28 | 0.00 | 0.72 | 0.00 | 0.00 | 0.00 |
| S10_cartel | 18 | 0.33 | 0.00 | 0.67 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| S1_cartel | 18 | 0.28 | 0.00 | 0.72 | 0.00 | 0.00 | 0.00 | 0.00 | 1.00 |

Live arms (forced Nash price at round 10):

- LR1_nash: I over rounds 1-9 = +nan; keeps the forced Nash price in 62% of rounds 11-30 (11/18 branches hold it throughout)
- R10_nash: I over rounds 1-9 = +0.731; keeps the forced Nash price in 44% of rounds 11-30 (8/18 branches hold it throughout)
- R1_br: I over rounds 1-9 = +nan; keeps the forced Nash price in 100% of rounds 11-30 (18/18 branches hold it throughout)
- R1_nash: I over rounds 1-9 = +nan; keeps the forced Nash price in 75% of rounds 11-30 (13/18 branches hold it throughout)
- S10_cartel: I over rounds 1-9 = +0.740; keeps the forced Nash price in 30% of rounds 11-30 (5/18 branches hold it throughout)
- S1_cartel: I over rounds 1-9 = +nan; keeps the forced Nash price in 29% of rounds 11-30 (5/18 branches hold it throughout)
- F_own (replayed incumbent), same rounds 1-9: I = +0.732

## gpt41mini_PI_exp7 / qwen-qwen3-14b-deepinfra-nothink

Share of branches by held price. All bases | only the 2 bases where the predecessor's last price differs from p_c.

| arm | n | competitor | pred_last | pred_earlier | best_resp | other | asym: competitor | asym: pred_last | asym: pred_earlier |
|---|---|---|---|---|---|---|---|---|---|
| C1_nash | 18 | 0.39 | 0.17 | 0.44 | 0.00 | 0.00 | 0.25 | 0.75 | 0.00 |
| F_own | 18 | 0.50 | 0.06 | 0.44 | 0.00 | 0.00 | 0.75 | 0.25 | 0.00 |
| F_pred | 18 | 0.67 | 0.00 | 0.22 | 0.00 | 0.11 | 1.00 | 0.00 | 0.00 |
| Fix_system | 18 | 0.44 | 0.11 | 0.44 | 0.00 | 0.00 | 0.50 | 0.50 | 0.00 |
| ID_system | 18 | 0.50 | 0.06 | 0.44 | 0.00 | 0.00 | 0.75 | 0.25 | 0.00 |
| K_own | 18 | 0.28 | 0.17 | 0.33 | 0.00 | 0.22 | 0.25 | 0.75 | 0.00 |
| K_pred | 18 | 0.56 | 0.11 | 0.22 | 0.00 | 0.11 | 0.50 | 0.50 | 0.00 |
| LK_own | 18 | 0.22 | 0.22 | 0.33 | 0.00 | 0.22 | 0.00 | 1.00 | 0.00 |
| LR1_nash | 18 | 0.28 | 0.22 | 0.33 | 0.00 | 0.17 | 0.00 | 1.00 | 0.00 |
| L_free | 18 | 0.33 | 0.22 | 0.44 | 0.00 | 0.00 | 0.00 | 1.00 | 0.00 |
| R10_nash | 18 | 0.33 | 0.00 | 0.33 | 0.00 | 0.33 | 1.00 | 0.00 | 0.00 |
| R1_br | 18 | 0.28 | 0.06 | 0.00 | 0.67 | 0.00 | 0.75 | 0.25 | 0.00 |
| R1_nash | 18 | 0.28 | 0.17 | 0.33 | 0.00 | 0.22 | 0.25 | 0.75 | 0.00 |
| S10_cartel | 18 | 0.50 | 0.06 | 0.44 | 0.00 | 0.00 | 0.75 | 0.25 | 0.00 |
| S1_cartel | 18 | 0.50 | 0.06 | 0.44 | 0.00 | 0.00 | 0.75 | 0.25 | 0.00 |

Live arms (forced Nash price at round 10):

- LR1_nash: I over rounds 1-9 = +nan; keeps the forced Nash price in 18% of rounds 11-30 (3/18 branches hold it throughout)
- R10_nash: I over rounds 1-9 = +0.891; keeps the forced Nash price in 33% of rounds 11-30 (6/18 branches hold it throughout)
- R1_br: I over rounds 1-9 = +nan; keeps the forced Nash price in 66% of rounds 11-30 (11/18 branches hold it throughout)
- R1_nash: I over rounds 1-9 = +nan; keeps the forced Nash price in 22% of rounds 11-30 (4/18 branches hold it throughout)
- S10_cartel: I over rounds 1-9 = +0.891; keeps the forced Nash price in 50% of rounds 11-30 (9/18 branches hold it throughout)
- S1_cartel: I over rounds 1-9 = +nan; keeps the forced Nash price in 50% of rounds 11-30 (9/18 branches hold it throughout)
- F_own (replayed incumbent), same rounds 1-9: I = +0.891
