
"""Summarize a Monday-Sunday week of daily logs.

Usage: python scripts/summarize_week.py 2026-02-09
Only recorded measurements enter averages. Missing days and legacy status
ambiguity are reported rather than filled in.
"""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path
import math
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
VALID_STATUSES = {"completed", "planned", "missed", "rest"}


def parse_front_matter(md_text: str) -> dict[str, str]:
    """Read only the first complete YAML-style front matter block."""
    lines = md_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        if ":" in line and not line.lstrip().startswith("#"):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip("\"'")
    return {}  # An unclosed block is not valid front matter.


def number(value: str) -> float | None:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) and parsed >= 0 else None


def training_status(fields: dict[str, str]) -> str:
    """Classify explicit status; retain uncertainty in older logs."""
    explicit = fields.get("training_status", "").lower()
    if explicit in VALID_STATUSES:
        return explicit
    if explicit:
        return "unknown (invalid status)"
    legacy = fields.get("training", "").lower()
    if legacy.endswith("(completed)"):
        return "completed"
    if "(planned" in legacy:
        return "planned"
    if legacy == "rest":
        return "no workout; reason unknown"
    return "unknown"


def main() -> int:
    # Windows redirected terminals may otherwise default to a legacy code page.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    try:
        start = date.fromisoformat(sys.argv[1])
    except ValueError:
        print("Enter a valid Monday date as YYYY-MM-DD.", file=sys.stderr)
        return 2
    if start.weekday() != 0:
        print("Enter the Monday that starts the check-in week.", file=sys.stderr)
        return 2

    weights: list[float] = []
    sleeps: list[float] = []
    statuses: dict[str, int] = {}
    missing: list[str] = []
    manual_review: list[str] = []
    warnings: list[str] = []
    structured = 0
    print(f"Week: {start.isoformat()} to {(start + timedelta(days=6)).isoformat()}")

    for offset in range(7):
        day = start + timedelta(days=offset)
        path = REPO_ROOT / "logs" / str(day.year) / f"{day.isoformat()}.md"
        if not path.exists():
            missing.append(day.isoformat())
            print(f"- {day.isoformat()} | log=missing")
            continue
        content = path.read_text(encoding="utf-8")
        fields = parse_front_matter(content)
        if not fields:
            manual_review.append(day.isoformat())
            if content.splitlines()[:1] == ["---"]:
                warnings.append(f"{day.isoformat()}: unclosed or empty front matter")
                print(f"- {day.isoformat()} | log=present; format=invalid front matter; manual review")
            else:
                print(f"- {day.isoformat()} | log=present; format=prose-only; manual review")
            continue
        structured += 1
        if fields.get("date") != day.isoformat():
            warnings.append(f"{day.isoformat()}: front matter date does not match filename")
        weight = number(fields.get("bodyweight_lb", ""))
        sleep = number(fields.get("sleep_hours", ""))
        if fields.get("bodyweight_lb") and weight is None:
            warnings.append(f"{day.isoformat()}: invalid bodyweight_lb")
        if fields.get("sleep_hours") and sleep is None:
            warnings.append(f"{day.isoformat()}: invalid sleep_hours")
        if weight is not None:
            weights.append(weight)
        if sleep is not None:
            sleeps.append(sleep)
        status = training_status(fields)
        if status == "unknown (invalid status)":
            warnings.append(f"{day.isoformat()}: invalid training_status")
        statuses[status] = statuses.get(status, 0) + 1
        session = fields.get("training", "") or "unspecified"
        print(
            f"- {day.isoformat()} | weight={f'{weight:g} lb' if weight is not None else '?'}"
            f" | sleep={f'{sleep:g} h' if sleep is not None else '?'}"
            f" | training={session} | status={status}"
        )

    def average(values: list[float], unit: str) -> str:
        if not values:
            return "unavailable (0/7 days)"
        return f"{sum(values) / len(values):.2f} {unit} ({len(values)}/7 days)"

    print(f"Average bodyweight: {average(weights, 'lb')}")
    print(f"Average sleep: {average(sleeps, 'h')}")
    print(f"Structured log coverage: {structured}/7 days")
    if statuses:
        print("Training status: " + ", ".join(f"{key}={count}" for key, count in sorted(statuses.items())))
    else:
        print("Training status: unavailable")
    print("Missing log dates: " + (", ".join(missing) if missing else "none"))
    print("Manual review dates: " + (", ".join(manual_review) if manual_review else "none"))
    print("Data warnings: " + ("; ".join(warnings) if warnings else "none"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
