"""
Market benchmarks for the inherited-collusion analysis (T1), taken from the environment itself.

    p_N   Nash price: OligopolyGame.lower_prices (the environment's own first-order-condition solve)
    p_M   monopoly price: OligopolyGame.upper_prices
    BR(p) the newcomer's static best response to an incumbent price p: the price in
          [unit cost, maximum willingness to pay] maximising its one-round profit

Profits use the same formula as OligopolyGame.step(); test() checks the two agree to 1e-9 and that
p_N is a fixed point of BR. Run: uv run python analysis/benchmarks.py
"""

from __future__ import annotations

import os
import sys

import numpy as np
from scipy.optimize import minimize_scalar

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from environment.oligopoly import OligopolyGame  # noqa: E402

DEFAULT_MARKET = dict(alpha=1.0, a0=0, ais=[2, 2], costs=[1, 1], mu=0.25, beta=100.0)


class Benchmarks:
    def __init__(self, **market):
        self.env = OligopolyGame(**{**DEFAULT_MARKET, **market}, verbose=False)
        self.nash = float(self.env.lower_prices[0])
        self.monopoly = float(self.env.upper_prices[0])
        self.max_wtp = round(1.5 * self.env.upper_prices[0], 2)  # the ceiling shown in the prompt

    def profits(self, prices) -> np.ndarray:
        """One-round profits for a price vector, exactly as OligopolyGame.step() computes them."""
        e = self.env
        base = np.exp(e.a0 / e.mu)
        d = np.exp((np.array(e.ais) - np.array(prices) / np.array(e.alpha_vec)) / e.mu)
        d = e.beta * d / (d.sum() + base)
        return d * (np.array(prices) - e.alpha * np.array(e.costs))

    def best_response(self, p_incumbent: float, newcomer: int = 1) -> float:
        """Static best response of firm `newcomer` to the other firm pricing at p_incumbent."""
        lo = self.env.alpha * self.env.costs[newcomer]

        def neg(p):
            prices = [p_incumbent] * self.env.nagents
            prices[newcomer] = p
            return -self.profits(prices)[newcomer]

        grid = np.linspace(lo, self.max_wtp, 2001)
        g = grid[int(np.argmin([neg(p) for p in grid]))]
        step = grid[1] - grid[0]
        res = minimize_scalar(neg, bounds=(max(lo, g - step), min(self.max_wtp, g + step)), method="bounded",
                              options={"xatol": 1e-8})
        return float(res.x)

    def inheritance_index(self, newcomer_price: float, p_c: float) -> float:
        """I = (price - BR(p_c)) / (p_c - BR(p_c)): 0 = best response, 1 = the cartel price."""
        br = self.best_response(p_c)
        return (newcomer_price - br) / (p_c - br)

    def price_index(self, price: float) -> float:
        """(price - p_N) / (p_M - p_N): 0 = Nash, 1 = monopoly."""
        return (price - self.nash) / (self.monopoly - self.nash)


def test():
    bm = Benchmarks()
    print(f"Nash      {bm.nash:.4f}   (Riemer et al. ~1.473)")
    print(f"Monopoly  {bm.monopoly:.4f}   (Riemer et al. ~1.925)")
    print(f"Max WTP   {bm.max_wtp:.2f}   (prompt ceiling)")
    assert abs(bm.nash - 1.473) < 0.005 and abs(bm.monopoly - 1.925) < 0.005

    # profits() agrees with the environment's step()
    rng = np.random.default_rng(0)
    for _ in range(200):
        prices = list(np.round(rng.uniform(1.0, 2.9, 2), 2))
        env = OligopolyGame(**DEFAULT_MARKET, verbose=False)
        _, _, step_profits, _, _ = env.step(prices)
        assert np.allclose(step_profits, bm.profits(prices), atol=1e-9)

    # Nash is a fixed point of BR; BR lies below the incumbent price above Nash
    assert abs(bm.best_response(bm.nash) - bm.nash) < 1e-4
    print("\n  p_c    BR(p_c)   p_c - BR")
    for p in [bm.nash, 1.6, 1.7, 1.8, bm.monopoly, 2.0, 2.2, 2.5]:
        br = bm.best_response(p)
        print(f"  {p:.3f}  {br:.4f}    {p - br:+.4f}")
        if p > bm.nash + 1e-6:
            assert br < p
    assert abs(bm.inheritance_index(bm.best_response(1.8), 1.8)) < 1e-9
    assert abs(bm.inheritance_index(1.8, 1.8) - 1) < 1e-9
    print("\nall benchmark checks pass")


if __name__ == "__main__":
    test()
