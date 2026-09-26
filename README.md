# Workout and diet log

This repository records actual training and food intake alongside a plan. Dated logs are the record of what happened; the profile and plan are working targets.

## Active plan as of 2026-09-26

- Goal: gradual cut toward about 151 lb while building or retaining strength, calisthenics skills, running stamina, and mobility.
- Last numeric bodyweight in the tracked logs: 175 lb on 2026-07-31. The profile's 173-177 lb range is a planning snapshot, not a current trend.
- Nutrition starting point: 1,900 kcal/day, with a flexible 1,800-2,000 kcal range and 160-180 g/day protein. Review plan/diet-plan.md before changing these provisional targets.
- Training: plan/workout-plan.md v3 has two hybrid strength days, one protected pure-calisthenics day, three Just Run days, and one rest day. Its restart ramp allows 4-5 completed sessions while rebuilding consistency. Follow the next Just Run workout rather than adding separate interval or tempo sessions.

## Daily logging

1. Use the local date in America/Los_Angeles. Start a new entry from logs/_template_daily_log.md at logs/YYYY/YYYY-MM-DD.md.
2. In new structured logs, training names the session (upper_hybrid, lower_hybrid, just_run, pure_calisthenics, rest, or other). training_status is completed, planned, missed, or rest. A planned session is not completed until confirmed; record any replacement on its actual date.
3. Record meals with portions and label data when available. Mark calculated calories and macros as estimates, and identify partial-day totals.
4. Log sleep, bodyweight, steps, hydration, effort, and pain only when reported. Leave missing measurements blank.

Existing logs use mixed formats, including prose-only entries. Preserve their facts and dates. Status metadata was added to the older February logs only where their own text made the outcome clear. February 14 remains a day with no workout but an unclear reason; February 15 remains a planned make-up with no confirmed completion.

## Weekly review

Run the summary with the Monday of the week:

    python scripts/summarize_week.py 2026-09-21

Then fill tracking/weekly-checkin.md. The script calculates bodyweight and sleep averages only from numeric front matter values and reports their sample counts. It flags prose-only logs for manual review; it does not infer missing measurements or completion from free text. A missing date is missing data, never a rest day. tracking/measurements.csv is an optional index and currently has no rows; the dated logs are the source of truth.

As of 2026-09-26, there are 36 tracked daily logs through September 25: 21 have front matter and 15 are prose-only. Only four logs have a numeric bodyweight (February 9-11 and July 31), so the repository cannot establish a recent weight-loss rate or measured maintenance calories. The September 20-25 entries do document a six-session sequence, but many recovery and bodyweight fields remain blank. Do not adjust calories from a sparse weekly average.

## File map

- config/profile.yml: current stated goals and provisional targets; confirm dated measurements before treating them as current.
- plan/workout-plan.md: active v3 sessions, schedule, home fallbacks, and progression rules.
- plan/diet-plan.md: active cut target and adjustment rules.
- plan/evidence-check.md: source review and limits of the plan audit.
- plan/exercise-videos.md: exercise demonstrations for the active plan.
- plan/exercise-library.md: supplementary written form references.
- plan/future-roadmap.md: possible later goals, not the current workout prescription.
- plan/progression.md: short index pointing to the active progression rules.
- logs/: historical daily records and the template for new entries.
- tracking/: weekly review template and optional measurement index.
- scripts/summarize_week.py: read-only summary of structured log fields.
