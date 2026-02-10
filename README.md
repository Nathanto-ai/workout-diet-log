
# Workout + Diet Log (GitHub-friendly)

This repo is a **simple system**:
- follow the plan (workout + diet)
- log each day in Markdown
- run weekly check-ins
- adjust calories/training based on trends

## Quick start (5 minutes)

1. Edit **`/config/profile.yml`** with your real details.
2. Read **`/plan/workout-plan.md`** and do **Week 1**.
3. Follow **`/plan/diet-plan.md`** for your calories/macros.
4. Log today using **`/logs/_template_daily_log.md`**.
5. Every Sunday, do **`/tracking/weekly-checkin.md`**.


## Daily usage with chat

- In the morning, ask: **"What needs to be done today?"**
- After each workout/meal, send a quick update in chat.
- I can convert updates into your daily markdown log and macro summary.


## How to run this plan each week

1. **Pick your weekly cadence:** complete the 5 core days (Mon-Fri structure) and use Day 6 as optional recovery/Zone-2 if energy and sleep are decent.
2. **Train in the morning:** keep sessions ~45-70 minutes and stop most sets with 1-2 reps in reserve.
3. **Log same day:** record training, meals, sleep, and bodyweight in a daily log.
4. **Eat to targets:** follow the macro/calorie range from `plan/diet-plan.md` and prioritize protein minimums.
5. **Review every Sunday:** run the weekly check-in and change only one variable (usually calories) at a time.

## Repo layout

- `config/` — your profile + targets
- `plan/` — workout plan, diet plan, progression rules
- `logs/` — daily logs (Markdown)
- `tracking/` — check-in template + measurements CSV
- `scripts/` — optional helper script(s)

## Principles

- **Consistency beats optimal.**
- Track **trend** (weekly averages), not single-day fluctuations.
- Change **one thing at a time** (usually calories first).
