# Plan: Report And Submission Readiness

## Goal

Prepare final generated deliverables and ensure report numbers match mission output and rubric requirements.

## Current State

The expected deliverables are `outputs/report.md`, `outputs/savings.png`, `outputs/focus_export.csv`, plus a short write-up. The rubric emphasizes verification, test pass rate, baseline-vs-optimized analysis, per-lever savings, sustainability, and at least two measured extensions.

## Files Likely Touched

- `outputs/report.md`
- `outputs/savings.png`
- `outputs/focus_export.csv`
- Optional write-up file if requested by the user.

## Implementation Steps

1. Run `python missions/run_all.py` to regenerate mission outputs.
2. Run `python missions/m5_report.py` to regenerate final report artifacts.
3. Confirm the report includes baseline spend, optimized spend, total savings, per-lever savings, and sustainability.
4. Confirm extension results are captured in the report or a separate write-up.
5. Confirm the write-up states the assumptions and measured values for cache economics and reasoning budget.
6. Cross-check report numbers against mission output.
7. Run full verification commands.

## Acceptance Criteria

- [ ] `outputs/report.md` exists and includes baseline, optimized, total savings, and sustainability.
- [ ] `outputs/savings.png` exists and is readable.
- [ ] `outputs/focus_export.csv` exists.
- [ ] At least two extensions have measured results available for the write-up.
- [ ] The write-up records cache assumptions: average reads, write cost, read discount, and break-even result.
- [ ] The write-up records reasoning assumptions: optimized-cost attribution, Wh multiplier, 10% cap scenario, and avoidable spend/Wh.
- [ ] `python verify.py` passes.
- [ ] `pytest -q` passes.

## Verification

- [ ] `python missions/run_all.py`
- [ ] `python missions/m5_report.py`
- [ ] `python verify.py`
- [ ] `pytest -q`

## Risks

- Regenerated outputs may change if source logic changes during extension work.
- Report text must stay consistent with numeric mission output.

## Completion Notes

Report readiness now includes extension results, sustainability, and unchanged verification coverage.
