
"""Summarize logs for a given week.

Usage:
  python scripts/summarize_week.py 2026-02-09

This script is intentionally simple and safe to modify.
"""

from __future__ import annotations
import sys
from pathlib import Path
from datetime import date, timedelta
import re

RE_DATE = re.compile(r"^date:\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
RE_WEIGHT = re.compile(r"^bodyweight_lb:\s*(.*)\s*$", re.MULTILINE)

def parse_front_matter(md_text: str) -> dict:
    out = {}
    # ultra-simple parser (doesn't require PyYAML)
    for line in md_text.splitlines():
        if line.strip() == '---':
            continue
        if ':' in line:
            k, v = line.split(':', 1)
            out[k.strip()] = v.strip()
    return out

def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    start = date.fromisoformat(sys.argv[1])
    end = start + timedelta(days=7)

    logs_dir = Path('logs')
    if not logs_dir.exists():
        print('No logs/ directory found. Run from repo root.')
        return 1

    entries = []
    day = start
    while day < end:
        path = logs_dir / str(day.year) / f"{day.isoformat()}.md"
        if path.exists():
            md = path.read_text(encoding='utf-8')
            fm = parse_front_matter(md)
            entries.append((day, fm.get('bodyweight_lb', ''), fm.get('training', ''), fm.get('sleep_hours','')))
        day += timedelta(days=1)

    if not entries:
        print('No logs found in that week.')
        return 0

    print(f"Week: {start.isoformat()} → {(end - timedelta(days=1)).isoformat()}")
    for d, bw, tr, sl in entries:
        print(f"- {d.isoformat()} | bw={bw or '?'} | training={tr or '?'} | sleep={sl or '?'}")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
