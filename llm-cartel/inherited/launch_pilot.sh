#!/usr/bin/env bash
# Base-model pilot (2026-10-24): which model/prompt settles on a shared price NEAR monopoly?
# gpt-4.1-mini PC overshoots to 2.35-2.80 in 10/10 seeds; qwen3-14b no-think PC never leaves Nash.
set -u
cd "$(dirname "$0")/.."
export PATH="$HOME/.local/bin:$PATH"
run() {  # model prefix rounds seed
  tag=$(echo "$1_$2" | tr '/@+.:' '-----')
  uv run python run_game.py --models "$1" --prefix "$2" --rounds "$3" --seeds "$4" --out_dir results/pilot -y \
    > "logs/pilot/${tag}_seed$4.log" 2>&1 &
}
for s in 0 1; do
  run openai/gpt-4.1 PC 40 $s
  run qwen/qwen3-235b-a22b-2507 PC 40 $s
  run deepseek/deepseek-chat-v3.1 PC 40 $s
  run meta-llama/llama-3.3-70b-instruct PC 40 $s
  run openai/gpt-4.1-mini PI 40 $s
  run openai/gpt-4.1-mini P0 40 $s
  run "qwen/qwen3-14b@deepinfra" PC 30 $s     # thinking ON (slow)
done
wait
echo "pilot finished"
