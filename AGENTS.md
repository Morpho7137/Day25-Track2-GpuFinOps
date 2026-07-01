# Agent Instructions

## Project Context

This repository is a pure-Python GPU FinOps lab. It uses deterministic synthetic data, five mission scripts, and a small `finops/` engine to produce a baseline-vs-optimized GPU cost report.

The graded path requires no GPU, no cloud account, no API key, and no Docker.

## Working Rules

- Be formal and concise.
- Preserve deterministic behavior from `data/generate.py`.
- Do not edit files under `tests/` unless the user explicitly requests it.
- Do not hardcode outputs only to satisfy `verify.py` or tests.
- Keep changes focused on the requested mission, engine function, or report workflow.
- Prefer small, verifiable task slices over broad refactors.
- Treat generated files in `outputs/` as artifacts unless the task is specifically about deliverables.

## Verification Commands

Run these before marking source work complete:

```bash
python verify.py
pytest -q
```

Use targeted commands when working on one mission:

```bash
python missions/m1_efficiency_audit.py
python missions/m2_inference_levers.py
python missions/m3_purchasing.py
python missions/m4_allocation.py
python missions/m5_report.py
```

## Definition Of Done

A task is complete only when:

- The requested behavior is implemented and measurable.
- Acceptance criteria in the task plan are satisfied.
- `python verify.py` passes, unless the task explicitly documents why it cannot.
- `pytest -q` passes, unless the task explicitly documents why it cannot.
- Any changed report numbers are consistent with mission output.
- The relevant plan file under `.agent/plans/` is updated with completion notes.

## Planning Workflow

- Use `.agent/PLANS.md` as the index of active and completed plans.
- Use `.agent/plans/TEMPLATE.md` when creating a new task plan.
- Create or update a task-specific plan before non-trivial implementation.
- Keep each plan small enough for one focused implementation session.
