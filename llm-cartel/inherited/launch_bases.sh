#!/usr/bin/env bash
# T2 base runs: both firms on the same model, prefix $PREFIX (default PC; PI after the 10-24 pilot), window 100, 120 rounds, temp 1.0, seeds 0-9.
# One process per (model, seed) so the 20 runs go in parallel. Resumable (run_game.py resumes by default).
set -u
cd "$(dirname "$0")/.."
export PATH="$HOME/.local/bin:$PATH"
PREFIX=${PREFIX:-PC}
MODELS=${MODELS:-"qwen/qwen3-14b@deepinfra+nothink openai/gpt-4.1-mini"}
for model in $MODELS; do
  tag=$(echo "$model" | tr '/@+.' '----')
  for seed in 0 1 2 3 4 5 6 7 8 9; do
    uv run python run_game.py --models "$model" --prefix "$PREFIX" --rounds 120 --seeds $seed \
      --out_dir results/base -y > "logs/base/${tag}_${PREFIX}_seed${seed}.log" 2>&1 &
  done
done
wait
echo "all base runs finished"
