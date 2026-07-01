# Plan: Your Turn Extension Selection

## Goal

Select at least two graded "Your Turn" extensions and define the implementation order, measurements, and verification expectations.

## Current State

The rubric awards 20 points for at least two extensions. Candidate extensions include improved tier policy, MBU-aware right-sizing, cache economics, reasoning budget, and carbon-aware scheduling.

## Recommended Selection

1. Cache Economics Extension
2. Reasoning Budget Extension

These are recommended because they are tightly scoped, measurable, and align with existing Mission 2 and Mission 5 flows.

## Files Likely Touched

- `finops/pricing.py`
- `missions/m2_inference_levers.py`
- `missions/m5_report.py`

Do not edit `tests/` unless the user explicitly requests test changes.

## Implementation Steps

1. Run the baseline verification plan first.
2. Implement cache economics as its own task.
3. Record before/after Mission 2 savings and cache-specific findings.
4. Implement reasoning budget as its own task.
5. Record reasoning traffic share, cost share, Wh impact, and proposed cap rule.
6. Update final report readiness plan after both extensions are measurable.
7. Preserve existing mission return keys so current tests and `verify.py` remain compatible.

## Acceptance Criteria

- [ ] At least two extensions have working code.
- [ ] Each extension reports numeric before/after or segmented measurements.
- [ ] `python verify.py` still passes.
- [ ] `pytest -q` still passes.
- [ ] The final report or write-up can explain the result of each extension.

## Verification

- [ ] `python missions/m2_inference_levers.py`
- [ ] `python missions/m5_report.py`
- [ ] `python verify.py`
- [ ] `pytest -q`

## Risks

- Changing core pricing behavior can move savings outside the rubric's expected ranges.
- Extension output should add insight without breaking existing mission return contracts.

## Completion Notes

Selected cache economics and reasoning budget as the two graded extensions; implementation now reflects both in Mission 2 and Mission 5.
