# Workout and diet log

This repository keeps daily training and nutrition records alongside a working plan. Dated logs record what happened; the profile and plan describe current targets. See `AUDIT.md` for dated findings and data gaps.

## Quick start

1. Check `config/profile.yml` for current goals, equipment, and targets.
2. Follow the active sessions in `plan/workout-plan.md` and the targets in `plan/diet-plan.md`.
3. Create today's entry from `logs/_template_daily_log.md` at `logs/YYYY/YYYY-MM-DD.md`, using the profile's timezone.
4. Review the week with `tracking/weekly-checkin.md`.

## Daily logging

- Record completed training and meals on the date they happened. Keep planned, missed, completed, and rest days distinct.
- In new structured logs, use `training` for the session type and `training_status` for its outcome.
- Record portions and food-label values when available. Mark calculated calories and macros as estimates, and identify partial-day totals.
- Enter sleep, bodyweight, steps, hydration, effort, and symptoms only when reported. Leave unknown values blank.
- Preserve historical logs, including prose-only entries, rather than filling gaps by assumption.

## Weekly review

Run `python scripts/summarize_week.py YYYY-MM-DD` with the Monday that starts the week, then complete `tracking/weekly-checkin.md`.

The script summarizes numeric front matter fields and reports sample counts. Prose-only logs require manual review. A missing date does not imply rest, and a partial food log does not establish a full-day total. Use repeated observations and the adjustment rules in the active plans before changing targets.

## Repository map

- `config/profile.yml` — current profile and planning targets.
- `plan/` — active workout and diet plans, progression guidance, exercise references, and future roadmap.
- `logs/` — dated records and the daily template.
- `tracking/` — weekly review template and optional measurements index.
- `scripts/` — read-only summary helper.
- `AUDIT.md` — dated repository review and unresolved questions.
