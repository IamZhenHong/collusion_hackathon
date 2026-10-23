"""Qwen3-14B behind vLLM on Modal, for the inherited-collusion runs.

The repo's poseidon_compute.modal_serve pins vllm 0.6.6, which predates Qwen3, so this is a
separate, deployed (not ephemeral) server: one H100, at most one container, scales to zero
after 10 idle minutes. Weights are cached in a Modal volume so later cold starts skip the download.

    modal secret create inherited-vllm VLLM_API_KEY=<random>     # once
    modal deploy inherited/modal_vllm.py                         # prints the URL
    modal app stop inherited-vllm                                # stop billing immediately

Clients use the `modal:` provider in harness/providers.py (MODAL_VLLM_URL / MODAL_VLLM_KEY), which
sends chat_template_kwargs={"enable_thinking": False} so Qwen3 answers without a <think> block.
"""
import os
import subprocess

import modal

MODEL = os.environ.get("INHERITED_MODEL", "Qwen/Qwen3-14B")
GPU = os.environ.get("INHERITED_GPU", "H100")
PORT = 8000

app = modal.App("inherited-vllm")

image = (
    modal.Image.debian_slim(python_version="3.12")
    .uv_pip_install("vllm==0.10.2", "huggingface_hub[hf_transfer]")
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1", "VLLM_USE_V1": "1"})
)
hf_cache = modal.Volume.from_name("inherited-hf-cache", create_if_missing=True)
vllm_cache = modal.Volume.from_name("inherited-vllm-cache", create_if_missing=True)


@app.function(
    image=image,
    gpu=GPU,
    max_containers=1,          # never fan out to a second GPU
    scaledown_window=600,      # 10 idle minutes, then the GPU is released
    timeout=3600,
    secrets=[modal.Secret.from_name("inherited-vllm")],
    volumes={"/root/.cache/huggingface": hf_cache, "/root/.cache/vllm": vllm_cache},
)
@modal.concurrent(max_inputs=128)
@modal.web_server(port=PORT, startup_timeout=1200)
def serve():
    cmd = [
        "vllm", "serve", MODEL,
        "--served-model-name", MODEL,
        "--host", "0.0.0.0", "--port", str(PORT),
        "--api-key", os.environ["VLLM_API_KEY"],
        "--max-model-len", "8192",
        "--gpu-memory-utilization", "0.92",
        "--max-num-seqs", "128",
        "--enable-prefix-caching",
    ]
    subprocess.Popen(cmd)
