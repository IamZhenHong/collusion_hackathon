"""Checks for the inherited-collusion prompt hooks (run: uv run python tests/test_inherited_hooks.py).

1. Identity: with every new option unset, prompts are byte-identical to the original
   environment/oligopoly.py at the upstream commit, across prefixes, think mode, windows and firms.
2. Placement: each hook lands where the design says, and relabelling covers every pre-takeover field.
"""
import importlib.util
import random
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from environment.oligopoly import OligopolyGame  # noqa: E402

UPSTREAM = "d585a7b"  # poseidon-research/collusion_hackathon commit this fork starts from


def load_upstream():
    src = subprocess.run(
        ["git", "show", f"{UPSTREAM}:llm-cartel/environment/oligopoly.py"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    path = Path(tempfile.mkdtemp()) / "oligopoly_upstream.py"
    path.write_text(src)
    spec = importlib.util.spec_from_file_location("oligopoly_upstream", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.OligopolyGame


def play(env, rounds, rng):
    for _ in range(rounds):
        env.step([round(rng.uniform(1.0, 2.9), 2) for _ in range(env.nagents)])
    return [env.generate_prompt(i) for i in range(env.nagents)]


def test_identity():
    Old = load_upstream()
    n = 0
    for prefix in ["P0", "PC", "AC", "PI", "CD", "P0+B", "PC+BT", "P0+T", "AP", "MD"]:
        for think in (False, True):
            for window, rounds in [(100, 0), (100, 7), (100, 130), (10, 25), (0, 5)]:
                for market in [dict(ais=[2, 2], costs=[1, 1], mu=0.25),
                               dict(ais=[3, 3, 3], costs=[1, 1, 1], mu=0.315)]:
                    kw = dict(prefix=prefix, window_size=window, think=think, verbose=False, a0=0, **market)
                    a = play(Old(**kw), rounds, random.Random(rounds))
                    b = play(OligopolyGame(**kw), rounds, random.Random(rounds))
                    assert a == b, f"prompt differs: prefix={prefix} think={think} window={window} rounds={rounds}"
                    n += 1
    print(f"identity: {n} configurations byte-identical to upstream {UPSTREAM}")


def test_placement():
    env = OligopolyGame(
        prefix=["PC", "P0"], verbose=False,
        history_owner={1: "predecessor"}, takeover_round={1: 3},
        history_header={1: "HEADER first={first} takeover={takeover}"},
        after_history={1: "AFTER"}, before_answer={1: "BEFORE"}, system_suffix={1: "SUFFIX"},
    )
    play(env, 5, random.Random(0))
    sys_p, user = (m["content"] for m in env.generate_prompt(1))
    # relabelling: rounds 1-3 predecessor, 4-5 own; competitor label untouched; no 'My' leak before takeover
    for r in (1, 2, 3):
        block = user.split(f"Round {r}:")[1].split("Round")[0]
        assert "Previous manager's price" in block and "Previous manager's quantity sold" in block
        assert "Previous manager's profit earned" in block and "My " not in block and "Competitor's price" in block
    for r in (4, 5):
        block = user.split(f"Round {r}:")[1].split("+++")[0].split("Round")[0]
        assert "My price" in block and "Previous manager" not in block
    # order: history block closes -> header -> after -> 'Now you have' -> before -> format -> answer line
    order = ["+++++++++++++++++++++\n\nHEADER first=1 takeover=3", "AFTER", "Now you have all the necessary",
             "BEFORE", "Your reponse MUST be in the following format:", "My chosen price:"]
    pos = [user.index(o) for o in order]
    assert pos == sorted(pos), pos
    assert user.endswith("in the following format:\n\nMy chosen price: <just the number, nothing else>")
    assert sys_p.index("SUFFIX") < sys_p.index("Your reponse MUST")
    # agent 0 untouched
    assert "Previous manager" not in env.generate_prompt(0)[1]["content"]
    assert "SUFFIX" not in env.generate_prompt(0)[0]["content"]
    print("placement: all hooks in the specified positions; relabelling complete")


if __name__ == "__main__":
    test_identity()
    test_placement()
