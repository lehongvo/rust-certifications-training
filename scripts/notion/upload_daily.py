#!/usr/bin/env python3
"""
Parse make-plan*.md files và upload daily entries lên Notion Daily Plan database.

Usage:
  source .env && python3 _upload_daily.py [--week N] [--all]
    --week N    : upload only week N (e.g. 1)
    --weeks N-M : upload weeks N to M
    --all       : upload all 48 weeks (~365 days)
    (default)   : sample - upload week 1 only
"""
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
if not NOTION_API_KEY:
    print("ERROR: NOTION_API_KEY env var not set. Run: source .env")
    sys.exit(1)

NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"

# Load DB IDs (relative to this script, not cwd)
_IDS_PATH = Path(__file__).parent / ".notion_ids.json"
with open(_IDS_PATH) as f:
    IDS = json.load(f)
DAILY_PLAN_DB = IDS["databases"]["daily_plan"]

REPO = Path("/Users/vincent/rust-certifications-training")
TASK_DIR = REPO / "task"


def api(method, path, body=None):
    url = f"{BASE_URL}{path}"
    data = json.dumps(body).encode() if body else None
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} on {method} {path}")
        print(e.read().decode()[:500])
        raise


# ============================================================
# PARSER
# ============================================================

PHASE_FOR_WEEK = {
    **{w: ("Phase 1 — Foundation", f"M{((w-1)//4)+1}") for w in range(1, 13)},
    **{w: ("Phase 2 — Build", f"M{((w-1)//4)+1}") for w in range(13, 25)},
    **{w: ("Phase 3 — Polish + ZK", f"M{((w-1)//4)+1}") for w in range(25, 37)},
    **{w: ("Phase 4 — Interview Circuit", f"M{((w-1)//4)+1}") for w in range(37, 49)},
}

PHASE_FILES = {
    1: TASK_DIR / "make-plan.md",
    2: TASK_DIR / "make-plan-phase2.md",
    3: TASK_DIR / "make-plan-phase3.md",
    4: TASK_DIR / "make-plan-phase4.md",
}


def get_phase_num(week):
    if week <= 12:
        return 1
    elif week <= 24:
        return 2
    elif week <= 36:
        return 3
    else:
        return 4


def parse_makeplan(phase_num):
    """Parse a phase markdown file. Return list of (week, day_name, date, theme, body)."""
    filepath = PHASE_FILES[phase_num]
    content = filepath.read_text()

    # Track current week theme by scanning week headers
    week_themes = {}
    week_header_pattern = re.compile(
        r'####\s+◆\s+WEEK\s+(\d+)\s*\(W\d+\)[^\n]*\n\*\*Theme:\*\*\s*([^\n]+)',
        re.MULTILINE
    )
    for m in week_header_pattern.finditer(content):
        week_themes[int(m.group(1))] = m.group(2).strip()

    # Day pattern: **W{N} — {DAYNAME} {YYYY-MM-DD}**
    day_pattern = re.compile(
        r'\*\*W(\d+)\s*—\s*(\w+(?:DAY)?)\s+(\d{4}-\d{2}-\d{2})\*\*\s*\n((?:(?!\*\*W\d+).)*?)(?=\*\*W\d+\s*—\s*\w+|\*\*W\d+\s+DELIVERABLES|####\s+◆|---\s*\n*###|\Z)',
        re.DOTALL
    )

    days = []
    for m in day_pattern.finditer(content):
        week = int(m.group(1))
        day_name = m.group(2).strip()
        date_str = m.group(3)
        body = m.group(4).strip()
        theme = week_themes.get(week, "")
        days.append({
            "week": week,
            "day_name": day_name,
            "date": date_str,
            "theme": theme,
            "body": body,
        })
    return days


def extract_tasks(body):
    """Extract checkbox tasks from markdown body. Return list of task strings."""
    tasks = []
    # Match "[ ] task text" lines
    for line in body.split("\n"):
        m = re.match(r'\s*\[\s\]\s+(.+)$', line)
        if m:
            tasks.append(m.group(1).strip())
    return tasks


def extract_section_blocks(body):
    """Convert body markdown to Notion blocks. Return list of block objects.

    Logic: parse line-by-line. Track if we're inside a ``` code fence.
    Inside code fences, we extract section headers (H3) + tasks (to_do) + sub-bullets.
    Outside code fences, we render prose as paragraphs.
    """
    blocks = []
    in_code = False
    current_section = None

    for raw_line in body.split("\n"):
        line = raw_line.rstrip()
        stripped = line.strip()

        # Toggle code fence
        if stripped.startswith("```"):
            in_code = not in_code
            continue

        if not stripped:
            continue

        # Skip blockquotes (the "Hôm nay là ngày đầu tiên" italic lines)
        if stripped.startswith(">"):
            continue

        if in_code:
            # Section header: "LEARN (2h):" or "BUILD CONTINUE:" etc.
            # Match all-caps words optionally with parens, ending with colon
            section_match = re.match(
                r'^([A-Z][A-Z\s/+\-]+(?:\s*\([^)]+\))?):\s*$',
                stripped
            )
            if section_match:
                current_section = section_match.group(1).strip()
                blocks.append({
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {
                        "rich_text": [{"type": "text", "text": {"content": current_section[:200]}}]
                    }
                })
                continue

            # Task: [ ] task text  (top-level, not indented)
            task_match = re.match(r'^\[\s\]\s+(.+)$', stripped)
            indent_chars = len(line) - len(line.lstrip())
            if task_match and indent_chars == 0:
                task_text = task_match.group(1).strip()
                if len(task_text) > 1900:
                    task_text = task_text[:1900] + "..."
                blocks.append({
                    "object": "block",
                    "type": "to_do",
                    "to_do": {
                        "rich_text": [{"type": "text", "text": {"content": task_text}}],
                        "checked": False,
                    }
                })
                continue

            # Indented [ ] sub-task (inside a parent task) — make it nested to_do
            if task_match and indent_chars > 0:
                task_text = task_match.group(1).strip()
                if len(task_text) > 1900:
                    task_text = task_text[:1900] + "..."
                blocks.append({
                    "object": "block",
                    "type": "to_do",
                    "to_do": {
                        "rich_text": [{"type": "text", "text": {"content": "    " + task_text}}],
                        "checked": False,
                    }
                })
                continue

            # Indented detail lines (URL:, Steps:, sub-bullets) → bulleted_list_item
            if indent_chars > 0 and current_section:
                detail_text = stripped
                if len(detail_text) < 1900:
                    blocks.append({
                        "object": "block",
                        "type": "bulleted_list_item",
                        "bulleted_list_item": {
                            "rich_text": [{"type": "text", "text": {"content": detail_text}}]
                        }
                    })
                continue

            # Other code-block lines (e.g., code snippets, raw content)
            # → render as code block fragment? For simplicity, render as paragraph with mono.
            if len(stripped) < 1900:
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{
                            "type": "text",
                            "text": {"content": stripped[:1900]},
                            "annotations": {"code": True}
                        }]
                    }
                })
        else:
            # Outside code fence: prose (italic notes, etc.)
            text = re.sub(r'^\*+(.+?)\*+$', r'\1', stripped)
            if len(text) > 0 and len(text) < 1900:
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": text}}]
                    }
                })

    return blocks[:90]  # Notion block limit safety (max 100 children per request)


# ============================================================
# UPLOAD
# ============================================================

def upload_day(day):
    """Create a Notion page in Daily Plan DB for a single day."""
    week = day["week"]
    phase_num = get_phase_num(week)
    phase_label, month_label = PHASE_FOR_WEEK[week]

    # Day name normalization
    day_name = day["day_name"].upper()
    if day_name in ["MON", "MONDAY"]:
        short_day = "Mon"
    elif day_name in ["TUE", "TUESDAY"]:
        short_day = "Tue"
    elif day_name in ["WED", "WEDNESDAY"]:
        short_day = "Wed"
    elif day_name in ["THU", "THURSDAY"]:
        short_day = "Thu"
    elif day_name in ["FRI", "FRIDAY"]:
        short_day = "Fri"
    elif day_name in ["SAT", "SATURDAY"]:
        short_day = "Sat"
    elif day_name in ["SUN", "SUNDAY"]:
        short_day = "Sun"
    else:
        short_day = day_name[:3]

    title = f"W{week} {short_day} {day['date']} — {day['theme'][:40]}" if day['theme'] else f"W{week} {short_day} {day['date']}"

    tasks = extract_tasks(day["body"])
    # Brief count summary for table view (not full bullet list — checkboxes are in page body)
    tasks_summary = f"{len(tasks)} tasks (xem trong page body để check off)" if tasks else "(rest day)"

    # Determine hours target based on day name
    if day_name in ["SAT", "SATURDAY"]:
        hours_target = 4
    elif day_name in ["SUN", "SUNDAY"]:
        hours_target = 0  # Rest day
    else:
        hours_target = 3

    # Build page properties
    props = {
        "Name": {"title": [{"text": {"content": title[:2000]}}]},
        "Date": {"date": {"start": day["date"]}},
        "Week": {"number": week},
        "Phase": {"select": {"name": phase_label}},
        "Month": {"select": {"name": month_label}},
        "Theme": {"rich_text": [{"text": {"content": day["theme"][:1900]}}]},
        "Hours_Target": {"number": hours_target},
        "Tasks": {"rich_text": [{"text": {"content": tasks_summary[:1900]}}]},
        "Status": {"select": {"name": "Not Started"}},
    }

    # Build page body (Notion blocks with full task detail)
    children = extract_section_blocks(day["body"])

    body = {
        "parent": {"database_id": DAILY_PLAN_DB},
        "properties": props,
        "children": children,
    }

    api("POST", "/pages", body)


# ============================================================
# MAIN
# ============================================================

def main():
    args = sys.argv[1:]

    target_weeks = set()
    if not args:
        # Default: only week 1 (sample)
        target_weeks = {1}
        mode = "sample (W1 only)"
    elif "--all" in args:
        target_weeks = set(range(1, 49))
        mode = "all 48 weeks"
    elif "--week" in args:
        idx = args.index("--week")
        target_weeks = {int(args[idx+1])}
        mode = f"week {args[idx+1]}"
    elif "--weeks" in args:
        idx = args.index("--weeks")
        rng = args[idx+1]
        a, b = map(int, rng.split("-"))
        target_weeks = set(range(a, b+1))
        mode = f"weeks {a}-{b}"
    else:
        print(__doc__)
        sys.exit(1)

    print("=" * 60)
    print(f"UPLOAD MODE: {mode}")
    print(f"Daily Plan DB: {DAILY_PLAN_DB}")
    print("=" * 60)

    # Determine which phase files to parse
    phases_needed = set()
    for w in target_weeks:
        phases_needed.add(get_phase_num(w))

    all_days = []
    for phase_num in sorted(phases_needed):
        print(f"\n→ Parsing Phase {phase_num} ({PHASE_FILES[phase_num].name})...")
        days = parse_makeplan(phase_num)
        days_in_target = [d for d in days if d["week"] in target_weeks]
        print(f"  Found {len(days)} day entries in file ({len(days_in_target)} matching target weeks)")
        all_days.extend(days_in_target)

    print(f"\n→ Total days to upload: {len(all_days)}")
    if not all_days:
        print("  Nothing to upload. Exit.")
        return

    print(f"  Estimated time: {len(all_days) * 0.5 / 60:.1f} min (at 0.5s per call)")
    print()

    success = 0
    failed = []
    for i, day in enumerate(all_days, 1):
        try:
            upload_day(day)
            success += 1
            print(f"  [{i}/{len(all_days)}] ✓ W{day['week']} {day['day_name']} {day['date']}")
        except Exception as e:
            failed.append((day, str(e)))
            print(f"  [{i}/{len(all_days)}] ✗ W{day['week']} {day['day_name']} {day['date']}: {e}")
        time.sleep(0.4)  # Rate limit

    print()
    print("=" * 60)
    print(f"UPLOAD COMPLETE — {success}/{len(all_days)} succeeded")
    if failed:
        print(f"FAILED: {len(failed)}")
        for day, err in failed[:5]:
            print(f"  - W{day['week']} {day['date']}: {err[:100]}")
    print("=" * 60)


if __name__ == "__main__":
    main()
