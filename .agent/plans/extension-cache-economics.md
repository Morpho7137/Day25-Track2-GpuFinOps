# Plan: Cache Economics Extension

## Goal

Add a cache break-even check so Mission 2 counts prompt-cache savings only when average cache reads justify the write or storage cost.

## Current State

`finops/pricing.py` already contains request-cost and discount-stack helpers. Mission 2 currently demonstrates cascade, cache, and batch savings. The extension should preserve the existing savings band required by `verify.py`.

## Files Likely Touched

- `finops/pricing.py`
- `missions/m2_inference_levers.py`

Do not edit `tests/` unless the user explicitly requests test changes.

## Implementation Steps

1. Inspect `request_cost`, `discount_stack`, and Mission 2's current cache calculation.
2. Add `cache_is_worth_it(avg_cache_reads, write_cost_per_m, read_discount=0.10)` to `finops/pricing.py`.
3. Define break-even with normalized units: `avg_cache_reads * (1 - read_discount) > write_cost_per_m`.
4. Integrate the helper into Mission 2 so cache savings are counted only when the threshold is met.
5. Use default Mission 2 assumptions: `avg_cache_reads = 3.0`, `write_cost_per_m = 1.0`, `read_discount = 0.10`.
6. Print and return the observed cache-read assumption, write-cost assumption, break-even result, and effective savings impact.
7. Add the new return data under `cache_economics` without changing existing return keys.

## Acceptance Criteria

- [ ] `cache_is_worth_it()` returns `True` above break-even and `False` below break-even.
- [ ] Mission 2 reports whether cache is economically justified.
- [ ] Mission 2 preserves existing return keys: `baseline_daily`, `optimized_daily`, `baseline_per_m`, `optimized_per_m`, `savings_pct`, and `total_tokens`.
- [ ] Mission 2 savings remain in the 60-95% band required by `verify.py`.
- [ ] The extension produces a numeric result suitable for the final write-up.

## Verification

- [ ] `python missions/m2_inference_levers.py`
- [ ] `python verify.py`
- [ ] `pytest -q`

## Risks

- An overly strict threshold could remove too much cache savings and fail the M2 savings band.
- The helper must be generic enough for tests without overfitting to the current dataset.
- The default assumptions must be stated in output or completion notes so the final write-up is auditable.

## Completion Notes

Implemented in Mission 2 with default assumptions, return-data support, and report output.
