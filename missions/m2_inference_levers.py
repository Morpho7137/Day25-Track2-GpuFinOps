"""M2 — Inference Cost Levers: $/1M-token, batch x cache x cascade (deck §7).

Run: python missions/m2_inference_levers.py
"""
from __future__ import annotations
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
from missions._common import load_csv, num
from finops import pricing, sustainability

# $/1M tokens (input, output) — illustrative 2026.
MODEL_PRICES = {"small": (0.20, 0.40), "large": (3.00, 15.00)}
DEFAULT_CACHE_READS = 3.0
DEFAULT_CACHE_WRITE_COST_PER_M = 1.0
DEFAULT_CACHE_READ_DISCOUNT = 0.10


def run(verbose: bool = True) -> dict:
    rows = load_csv("token_usage.csv")
    base_cost = opt_cost = 0.0
    total_tokens = 0
    reasoning_cost = reasoning_tokens = 0.0
    non_reasoning_cost = non_reasoning_tokens = 0.0
    cached_input_tokens = total_input_tokens = 0
    reasoning_wh = non_reasoning_wh = 0.0
    for r in rows:
        inp, out = int(num(r["input_tokens"])), int(num(r["output_tokens"]))
        cached = int(num(r["cached_input_tokens"]))
        is_batch = bool(int(num(r["is_batch"])))
        is_reasoning = bool(int(num(r["is_reasoning"])))
        total_tokens += inp + out
        total_input_tokens += inp
        cached_input_tokens += cached
        # BASELINE: naive deployment — everything on the large model, no cache, no batch
        lin, lout = MODEL_PRICES["large"]
        row_base_cost = pricing.request_cost(inp, out, lin, lout)
        base_cost += row_base_cost
        # OPTIMIZED: cascade (route_tier), prompt caching, batch API
        pin, pout = MODEL_PRICES[r["route_tier"]]
        row_opt_cost = pricing.request_cost(inp, out, pin, pout, cached_in=cached, batch=is_batch)
        opt_cost += row_opt_cost

        if is_reasoning:
            reasoning_cost += row_opt_cost
            reasoning_tokens += inp + out
            reasoning_wh += sustainability.wh_per_query(inp + out, is_reasoning=True)
        else:
            non_reasoning_cost += row_opt_cost
            non_reasoning_tokens += inp + out
            non_reasoning_wh += sustainability.wh_per_query(inp + out, is_reasoning=False)

    base_pm = pricing.dollars_per_million(base_cost, total_tokens)
    opt_pm = pricing.dollars_per_million(opt_cost, total_tokens)
    savings_pct = (1 - opt_cost / base_cost) * 100 if base_cost else 0.0

    cache_hit_frac = (cached_input_tokens / total_input_tokens) if total_input_tokens else 0.0
    cache_worth_it = pricing.cache_is_worth_it(
        DEFAULT_CACHE_READS,
        DEFAULT_CACHE_WRITE_COST_PER_M,
        DEFAULT_CACHE_READ_DISCOUNT,
    )
    cache_effective_savings = (
        opt_cost * cache_hit_frac * (1.0 - DEFAULT_CACHE_READ_DISCOUNT)
        if cache_worth_it
        else 0.0
    )
    reasoning_share = (reasoning_tokens / total_tokens) if total_tokens else 0.0
    reasoning_cost_share = (reasoning_cost / opt_cost) if opt_cost else 0.0
    non_reasoning_cost_share = (non_reasoning_cost / opt_cost) if opt_cost else 0.0
    reasoning_cap_share = 0.10
    capped_reasoning_cost = reasoning_cost * reasoning_cap_share
    capped_reasoning_wh = reasoning_wh * reasoning_cap_share
    avoidable_reasoning_cost = reasoning_cost - capped_reasoning_cost
    avoidable_reasoning_wh = reasoning_wh - capped_reasoning_wh

    if verbose:
        print("== M2 Inference Cost Levers ==")
        print(f"requests={len(rows)}  tokens={total_tokens:,}")
        print(f"baseline  : ${base_cost:,.2f}/day   ${base_pm:.3f}/1M-token")
        print(f"optimized : ${opt_cost:,.2f}/day   ${opt_pm:.3f}/1M-token")
        print(f"savings   : {savings_pct:.1f}%  (cascade + caching + batch)")
        print(f"discount stack (batch + 100% cache): {pricing.discount_stack(batch=True, cache_hit_frac=1.0):.3f} of naive")
        print(
            "cache economics: "
            f"reads={DEFAULT_CACHE_READS:.1f}, write_cost={DEFAULT_CACHE_WRITE_COST_PER_M:.1f}, "
            f"read_discount={DEFAULT_CACHE_READ_DISCOUNT:.2f}, worth_it={cache_worth_it}"
        )
        print(
            "reasoning budget: "
            f"share={reasoning_share:.1%}, cost_share={reasoning_cost_share:.1%}, "
            f"wh={reasoning_wh:.2f}, cap10% avoidable=${avoidable_reasoning_cost:.2f}, "
            f"avoid_wh={avoidable_reasoning_wh:.2f}"
        )

    return {
        "baseline_daily": round(base_cost, 2), "optimized_daily": round(opt_cost, 2),
        "baseline_per_m": round(base_pm, 3), "optimized_per_m": round(opt_pm, 3),
        "savings_pct": round(savings_pct, 1), "total_tokens": total_tokens,
        "cache_economics": {
            "avg_cache_reads": DEFAULT_CACHE_READS,
            "write_cost_per_m": DEFAULT_CACHE_WRITE_COST_PER_M,
            "read_discount": DEFAULT_CACHE_READ_DISCOUNT,
            "worth_it": cache_worth_it,
            "cache_hit_frac": round(cache_hit_frac, 4),
            "effective_savings_usd": round(cache_effective_savings, 2),
        },
        "reasoning_budget": {
            "reasoning_share": round(reasoning_share, 4),
            "reasoning_cost_share": round(reasoning_cost_share, 4),
            "non_reasoning_cost_share": round(non_reasoning_cost_share, 4),
            "reasoning_wh": round(reasoning_wh, 2),
            "non_reasoning_wh": round(non_reasoning_wh, 2),
            "cap_share": reasoning_cap_share,
            "avoidable_cost_usd": round(avoidable_reasoning_cost, 2),
            "avoidable_wh": round(avoidable_reasoning_wh, 2),
        },
    }


if __name__ == "__main__":
    run()
