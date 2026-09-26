# Repository audit — 2026-09-26

## Baseline and scope

This audit uses `origin/main` at `ccd0cf3` after a fetch on 2026-09-26, plus the local, unpushed alignment work on top of it. All 51 tracked files were inventoried. The review covered the repository instructions, profile, seven plan files, template, all 36 dated logs, two tracking files, summary script, README, and ignore rules. No remote branch was changed.

The dated logs are evidence of reported activity; the profile and plan are intended targets. A plan passing a coverage review does not prove that the user followed it or recovered well from it.

## Findings and actions

| Priority | Finding | Evidence | Action or limit |
| --- | --- | --- | --- |
| High | The profile said no pain was reported, but recurrent low-left-back/lat symptoms were documented. | Logs on 2026-08-02, 2026-08-13, 2026-08-27, and 2026-09-22. | Corrected the profile and retained the dated observations in this audit. The standing workout plan does not prescribe a change from these records; current symptoms remain unknown. |
| High | The calorie target cannot yet be tested against a recent weight trend. | Four numeric bodyweights exist: 2026-02-09 through 2026-02-11 and 2026-07-31. The last value is 175 lb. | Kept 1,900 kcal and 160-180 g protein as provisional targets. Use new, repeated weight and recovery data before changing them. |
| Medium | Automated weekly summaries have limited coverage. | Of 36 logs, 21 have front matter and 15 are prose-only. Only 9 structured logs have an explicit `training_status`; 12 do not. Only 3 logs have numeric sleep. `tracking/measurements.csv` has a header and no data rows. | The script reports sample counts and flags prose-only dates for manual review. Historical logs were not bulk-converted or given inferred measurements. |
| Medium | The restart guidance and recent effort diverged. | The plan calls for about 2-3 RIR in the restart phase; the 2026-09-20 and 2026-09-24 entries include sets at 0-1 RIR. | Keep the restart rule visible and use the logged RIR to scale the next session. This is an execution observation, not a reason to add more volume. |
| Medium | Lower-body resistance has one clearly hard bilateral session, while Day 5 is lighter skill/control work. | Day 3 and Day 5 prescriptions in `plan/workout-plan.md`; the current evidence check previously labeled lower-body coverage a full pass. | Qualified the evidence verdict. Monitor strength, soreness, and running before treating the dose as sufficient or increasing it. |
| Medium | Two recent complete food logs missed the fiber target, while one exceeded the flexible calorie ceiling. | 2026-09-24: about 1,925 kcal, 157 g protein, 19-21 g fiber. 2026-09-25: about 2,025 kcal, 152 g protein, 18-20 g fiber. The plan targets 25-35 g fiber and allows 1,800-2,000 kcal. | Do not infer a trend from two days. Keep meal estimates labeled and review fiber/produce at the next complete daily log. |

## Cross-file alignment

- **Active plan:** `plan/workout-plan.md` v3 supplies two hybrid resistance days, one calisthenics day, three Just Run sessions, and one rest day. `config/profile.yml`, `plan/diet-plan.md`, `tracking/weekly-checkin.md`, and `README.md` describe current targets and roles. `plan/progression.md` preserves the earlier v1 guide as an archived reference. `plan/future-roadmap.md` explicitly defers additional power, speed, and mobility-skill work; it does not prescribe extra sessions now.
- **Recent activity:** the 2026-09-20 through 2026-09-25 logs describe the six planned session types, including a reduced-volume lower session and some near-failure upper-body sets. They do not provide a recent bodyweight or sleep trend, nor a confirmed resolution of the recurring back/lat issue.
- **Nutrition:** the preferred Huel/milk plus dinner structure is a preference, not a requirement or a verified calorie prescription. Food entries distinguish labels from estimates where portions or catering recipes are uncertain. The 2026-09-24 and 2026-09-25 psyllium entries use the corrected label value of 30 kcal per two rounded teaspoons.
- **Logging:** new structured logs have a `training` session name and separate `training_status`. The February status additions are supported by their own text. The 2026-02-14 no-workout reason and 2026-02-15 planned make-up outcome remain unknown. Prose-only August and September logs remain readable historical records and require manual review.
- **References:** all eight research/app links in `plan/evidence-check.md` were opened during this audit; two PubMed pages returned a browser challenge on the current attempt, so their abstracts were not reverified this pass. All 39 distinct YouTube demo IDs returned metadata with the expected movement/channel, and the Vimeo URL returned HTTP 200. This checks availability and metadata, not every frame of instruction. The demo file already lists three unverified movement-specific gaps.

## Validation and outstanding information

Checks: file/date/front-matter inventory; `python -m py_compile scripts/summarize_week.py`; weekly summaries for 2026-02-09, 2026-02-16, and 2026-09-21; `git diff --check`; numbered review of changed files; `git status --short`. The script is read-only and does not infer completion, nutrition totals, or health status from prose.

Next useful observations are current morning bodyweight across multiple days, actual sleep/recovery, current back/lat symptom status, exact RIR and loads for key lifts, and complete meal/fiber logs. None should be fabricated from this repository.
