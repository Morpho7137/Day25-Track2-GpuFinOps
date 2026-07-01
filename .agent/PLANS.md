# Agent Plans

This file is the planning index for Codex sessions in this repository.

## Active Plans

| Plan | Status | Purpose |
|---|---|---|
| [Baseline Verification](plans/baseline-verification.md) | Ready | Establish the current project health before feature work. |
| [Your Turn Extension Selection](plans/your-turn-extension-selection.md) | Ready | Choose and scope at least two graded extensions. |
| [Cache Economics Extension](plans/extension-cache-economics.md) | Ready | Add cache break-even logic and Mission 2 integration. |
| [Reasoning Budget Extension](plans/extension-reasoning-budget.md) | Ready | Quantify reasoning traffic cost and energy impact. |
| [Report And Submission Readiness](plans/report-and-submission-readiness.md) | Ready | Prepare final generated deliverables and consistency checks. |

## Completed Plans

None yet.

## Deferred Plans

None yet.

## Planning Rules

- Start non-trivial work from a task-specific plan under `.agent/plans/`.
- Keep each task scoped to one mission, one `finops` module, or one deliverable workflow.
- Record verification commands and results in the relevant plan file.
- If a task changes report numbers, record the before/after values.
- Do not mark a plan complete until `python verify.py` and `pytest -q` have been considered.
- Do not edit `tests/` unless the user explicitly requests test changes.
