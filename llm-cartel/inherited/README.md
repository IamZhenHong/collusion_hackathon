# Inherited Collusion (Apart AI Collusion Sprint, Oct 2026)

Does replacing a colluding LLM pricing agent restore competition? Built on the `llm-cartel` harness
(Riemer et al.) in this fork of `poseidon-research/collusion_hackathon`.

- **Write-up:** [REPORT.md](REPORT.md) (draft)
- **Pre-registration:** [PREREG.md](PREREG.md); tags `ic-prereg-v1`, `ic-prereg-addendum1`, `ic-prereg-addendum2`
  mark the commits made before each batch ran.
- **Results:** `../results/analysis/<set>/contrasts.md` (decision rules), `../results/analysis/figures/`,
  `../results/analysis/branches.csv` (one row per branch), raw branches in `../results/branches/`, base runs
  in `../results/base/`.

## What was added to the harness

| File | Addition |
|---|---|
| `environment/oligopoly.py` | Optional per-agent prompt hooks: relabel inherited rows as a predecessor's, header / after-history / decision-point / system-suffix text. Off by default; prompts byte-identical to upstream (`tests/test_inherited_hooks.py`) |
| `branch_game.py` | Hooks for replaced agents; replayed incumbent (no model call); forced price rounds (Nash, cartel, best response); one-round incumbent cut; fake last row seen only by the newcomer; `--print_prompt` |
| `harness/providers.py` | `+nothink` (Qwen3 `/no_think`) and `@host` (pinned OpenRouter host) in model ids |
| `analysis/benchmarks.py` | Nash, monopoly and best-response prices from the environment's own code |
| `analysis/analyze.py`, `analysis/explore.py` | Pre-registered metrics and decision rules; exploratory held-price analysis; figures |
| `inherited/` | Arms, base selection, resumable shuffled runner, launchers, prompt review |

## Reproduce

```bash
./setup.sh llm-cartel                     # from the repo root; put OPENROUTER_API_KEY in compute.env
cd llm-cartel
uv run python tests/test_inherited_hooks.py
PREFIX=PI MODELS="openai/gpt-4.1-mini" ./inherited/launch_bases.sh
uv run python inherited/select_bases.py "results/base/2agents_prefix_PI-PI_*gpt-4p1-mini*.jsonl" --tag gpt41mini_PI
uv run python inherited/run_arms.py inherited/bases_gpt41mini_PI.json --newcomer openai/gpt-4.1-mini --experiments 1 2 3 4 5 --dry_run
uv run --with matplotlib python analysis/analyze.py
```

`inherited/modal_vllm.py` (a Qwen3-14B vLLM server on Modal) was written for an interpretability stretch
that was not run; it is untested.
