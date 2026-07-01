# Plan: Reasoning Budget Extension

## Goal

Quantify reasoning traffic cost and energy impact, then propose a routing cap that reduces spend and Wh while preserving the existing lab flow.

## Current State

`data/token_usage.csv` includes `is_reasoning`. Mission 2 handles inference cost levers, and Mission 5 builds the summary report. `finops/sustainability.py` contains energy and carbon helpers.

## Files Likely Touched

- `missions/m2_inference_levers.py`
- `missions/m5_report.py`
- `finops/sustainability.py` only if an existing helper cannot express the required calculation.

## Implementation Steps

1. Inspect how Mission 2 computes baseline and optimized request costs.
2. Segment token usage by `is_reasoning`.
3. Compute reasoning traffic share, optimized-cost share, and estimated Wh share.
4. Use `sustainability.wh_per_query(total_tokens, is_reasoning=True)` for reasoning rows and `is_reasoning=False` for non-reasoning rows.
5. Add a cap scenario that reduces reasoning requests to 10% of total traffic and reports avoidable attributed spend and Wh.
6. Surface the result in Mission 2 output or Mission 5 report data under `reasoning_budget`.
7. Ensure existing mission return keys used by tests remain unchanged.

## Acceptance Criteria

- [ ] Output separates reasoning and non-reasoning traffic.
- [ ] Output includes reasoning request share, cost share, and Wh impact.
- [ ] A concrete 10% reasoning cap or routing rule is reported.
- [ ] Dollar savings are labeled as attributed avoidable spend because the lab has no separate provider reasoning price multiplier.
- [ ] Existing M2 and M5 return keys remain compatible with tests and `verify.py`.
- [ ] Existing M2 and M5 verification ranges still pass.

## Verification

- [ ] `python missions/m2_inference_levers.py`
- [ ] `python missions/m5_report.py`
- [ ] `python verify.py`
- [ ] `pytest -q`

## Risks

- Adding report data must not break existing report formatting tests.
- Energy assumptions should reuse existing sustainability helpers where possible.
- If live provider pricing is later supplied, the attributed spend calculation can be replaced with real billing multipliers.

## Completion Notes

Implemented in Mission 2 and surfaced in Mission 5 report output and return data.
