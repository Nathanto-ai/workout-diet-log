# AGENTS.md

Purpose: lightweight operating manual for AI coding agents (and humans) working in this repo.
Scope: entire repository.

## Project goals
- Keep daily training/nutrition logging fast and accurate.
- Preserve historical data integrity (logs are append-only records unless fixing clear mistakes).
- Prefer simple, auditable markdown changes over complex automation.

## Repository map
- `logs/` daily entries and template.
- `plan/` workout/diet/progression guidance.
- `tracking/` durable tabular/weekly summaries.
- `scripts/` helper utilities.
- `config/profile.yml` profile targets and defaults.

## Working rules for agents
These follow common "agent instruction" patterns used in public AI coding workflows:

1. **Ask: is this a data update or plan update?**
   - Data updates: edit only the relevant date file(s) in `logs/`.
   - Plan updates: edit files in `plan/` and explain rationale.

2. **Minimize blast radius.**
   - Do not reformat unrelated sections.
   - Do not change past logs unless explicitly requested.

3. **Be explicit with assumptions.**
   - If calories/macros are estimated, label them as estimates.
   - Keep units explicit (`lb`, `oz`, `kcal`, `g`, `L`).

4. **Diet info should be evidence-checked, not guessed.**
   - Prefer user-provided food labels first.
   - If label data is missing and the user asks for precision, use a reputable source (e.g., USDA FoodData Central or manufacturer nutrition page) and cite it in your response.
   - If no reliable source is available quickly, provide a range and clearly state uncertainty.

5. **Consistency over cleverness.**
   - Reuse existing headings/structure from `logs/_template_daily_log.md`.
   - Keep naming and section order stable.

6. **Validation before commit.**
   - Run at least: `git status --short` and preview changed files with `nl -ba`.
   - If a script is touched, run the script or a relevant check.

7. **Commit discipline.**
   - One coherent commit per user request.
   - Commit message format: imperative and specific, e.g. `Log 2026-02-11 check-in metrics`.

## Daily log content checklist
When closing a day, include (if available):
- Sleep duration (and optional quality 1-5)
- Bodyweight
- Steps
- Training completed + key notes (or RPE)
- Nutrition entries + estimated totals
- Hydration
- Mood/energy and hunger
- Pain/soreness notes

## Non-goals
- Do not invent measurements the user did not provide.
- Do not present estimates as exact label values.
- Do not silently rewrite prior coaching conclusions.

## PR expectations
- Brief summary of what changed and why.
- List exact checks/commands run.
- Call out unresolved unknowns (missing user inputs).
