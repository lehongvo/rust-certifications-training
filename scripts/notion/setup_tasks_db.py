#!/usr/bin/env python3
"""
Tạo Daily Tasks sub-database + upload tất cả tasks (~3500 rows) với relation tới Daily Plan.
Mỗi task = 1 row, có checkbox riêng — hiển thị checkbox trực tiếp trong table view.

Usage:
  source .env && python3 _setup_tasks_db.py
"""
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
if not NOTION_API_KEY:
    print("ERROR: NOTION_API_KEY env var not set. Run: source .env")
    sys.exit(1)

NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"
PARENT_PAGE_ID = "3540a79c-06a3-814c-820d-d0373b562320"

_IDS_PATH = Path(__file__).parent / ".notion_ids.json"
with open(_IDS_PATH) as f:
    IDS = json.load(f)
DAILY_PLAN_DB = IDS["databases"]["daily_plan"]

REPO = Path("/Users/vincent/rust-certifications-training")
TASK_DIR = REPO / "task"
PHASE_FILES = {
    1: TASK_DIR / "make-plan.md",
    2: TASK_DIR / "make-plan-phase2.md",
    3: TASK_DIR / "make-plan-phase3.md",
    4: TASK_DIR / "make-plan-phase4.md",
}


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
        body_str = e.read().decode()[:300]
        raise Exception(f"HTTP {e.code}: {body_str}")


def get_phase_num(week):
    if week <= 12: return 1
    elif week <= 24: return 2
    elif week <= 36: return 3
    else: return 4


def parse_makeplan(phase_num):
    """Parse phase markdown. Return list of dicts với week, day_name, date, theme, body."""
    filepath = PHASE_FILES[phase_num]
    content = filepath.read_text()

    week_themes = {}
    for m in re.finditer(
        r'####\s+◆\s+WEEK\s+(\d+)\s*\(W\d+\)[^\n]*\n\*\*Theme:\*\*\s*([^\n]+)',
        content, re.MULTILINE
    ):
        week_themes[int(m.group(1))] = m.group(2).strip()

    day_pattern = re.compile(
        r'\*\*W(\d+)\s*—\s*(\w+(?:DAY)?)\s+(\d{4}-\d{2}-\d{2})\*\*\s*\n((?:(?!\*\*W\d+).)*?)(?=\*\*W\d+\s*—\s*\w+|\*\*W\d+\s+DELIVERABLES|####\s+◆|---\s*\n*###|\Z)',
        re.DOTALL
    )

    days = []
    for m in day_pattern.finditer(content):
        days.append({
            "week": int(m.group(1)),
            "day_name": m.group(2).strip(),
            "date": m.group(3),
            "theme": week_themes.get(int(m.group(1)), ""),
            "body": m.group(4).strip(),
        })
    return days


def parse_tasks_with_section(body):
    """Parse body và return list of (section, task_text, order)."""
    tasks = []
    in_code = False
    current_section = ""
    order = 0

    for raw_line in body.split("\n"):
        line = raw_line.rstrip()
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code = not in_code
            continue

        if not in_code or not stripped:
            continue

        # Section header
        section_match = re.match(r'^([A-Z][A-Z\s/+\-]+(?:\s*\([^)]+\))?):\s*$', stripped)
        if section_match:
            raw = section_match.group(1).strip()
            # Strip "(Xh)" / "(X-Yh)" / "(continued)" suffix to normalize
            current_section = re.sub(r'\s*\([^)]*\)\s*$', '', raw).strip()
            continue

        # Task: [ ] text
        task_match = re.match(r'^\[\s\]\s+(.+)$', stripped)
        if task_match:
            task_text = task_match.group(1).strip()
            if len(task_text) > 1900:
                task_text = task_text[:1900]
            order += 1
            tasks.append({
                "section": current_section or "GENERAL",
                "text": task_text,
                "order": order,
            })

    return tasks


# Common section names to pre-populate as Select options
SECTION_OPTIONS = [
    "SETUP", "LEARN", "BUILD", "TEST", "DEPLOY", "AUDIT", "SECURITY",
    "PRACTICE", "REVIEW", "COMMIT", "BLOG", "TWITTER", "APPLY",
    "INTERVIEW", "INTERVIEW PREP", "NETWORKING", "NETWORK", "CONTENT",
    "POLISH", "PERSONAL BRAND", "BOOTCAMP", "OSS", "OSS CONTRIBUTION",
    "DEEP WORK", "FRONTEND BUILD", "FRONTEND POLISH", "DESIGN",
    "MAINNET DEPLOY", "ANNOUNCEMENT", "POST-DEPLOY", "RECOVERY",
    "DOCUMENTATION", "RESEARCH", "GENERAL",
    "ONBOARDING", "ONBOARDING WEEK 2", "PHASE 4 KICKOFF", "PHASE 3 KICKOFF",
    "PHASE 2 KICKOFF", "PIPELINE STATUS CHECK", "INTERVIEW EXECUTION",
    "TAKE-HOME WORK", "DECISION RESEARCH", "FINAL ROUND PREP",
    "FINAL ROUND EXECUTION", "OFFER STATUS", "NEGOTIATE PREP",
    "NEGOTIATE EXECUTION", "ACCEPTANCE OR PUSH-BACK",
    "COMMUNICATION CASCADE", "RESTART", "DECISIVE",
    "INDEXING", "INTEGRATION TESTING", "INTERVIEW BLITZ",
    "INTERVIEW LOOP", "INTERVIEW INTENSE WEEK PREP",
    "INTERVIEW + APPLY", "INTERVIEW + RECOVERY", "LIGHT DAY",
    "LIGHT WORK", "LIGHT APPLY", "DAY OFF", "Q1 DECISION GATE EVALUATION",
    "Q2 DECISION GATE EVALUATION", "Q3 GATE EVALUATION",
    "PHASE 1 FINAL REVIEW", "PHASE 2 RETROSPECTIVE", "PHASE 3 RETROSPECTIVE",
    "PHASE 2 CLOSE", "PHASE 3 CLOSE", "PHASE 4 PLANNING", "PLAN PHASE 2",
    "BUFFER MODE", "BUFFER DAY", "BUILD CONTINUE", "AUDIT PRACTICE",
    "PRE-MAINNET CHECKLIST", "ENCODE CLUB FINAL", "ORACLE INTEGRATION",
    "TECH ROUND PREP", "TECH ROUND EXECUTION", "MAJOR DECISION FRAMEWORK",
    "CONTENT BLITZ", "TEST EXPANSION", "SECURITY AUDIT", "MOCK INTERVIEW",
    "LEARN ZK", "LEARN + APPLY", "REAL INTERVIEW",
    "SOLANA FOUNDATION BOOTCAMP", "FINAL COMMIT", "FINAL GATE EVALUATION",
    "ONE-YEAR ANNIVERSARY",
]

PHASE_LABELS = [
    "Phase 1 — Foundation",
    "Phase 2 — Build",
    "Phase 3 — Polish + ZK",
    "Phase 4 — Interview Circuit",
]


CANONICAL_SECTIONS = [
    "SETUP", "LEARN", "BUILD", "TEST", "DEPLOY", "AUDIT", "SECURITY",
    "REFACTOR", "REVIEW", "POLISH", "DOCUMENTATION", "DESIGN",
    "PRACTICE", "COMMIT", "BLOG", "TWITTER", "CONTENT", "PERSONAL BRAND",
    "APPLY", "INTERVIEW", "INTERVIEW PREP", "NETWORKING", "NEGOTIATE",
    "OFFER", "ONBOARDING", "BOOTCAMP", "OSS", "FRONTEND",
    "INTEGRATION TESTING", "MAINNET DEPLOY", "INDEXING", "RESEARCH",
    "DEEP WORK", "MORNING SESSION", "AFTERNOON SESSION",
    "DECISION GATE", "PHASE KICKOFF", "PHASE CLOSE", "PHASE PLANNING",
    "RETROSPECTIVE", "BUFFER DAY", "REST", "RECOVERY",
    "OFFER STATUS", "ANNOUNCEMENT", "ADMIN", "HEALTH",
    "PATH A", "PATH B", "PATH C", "EITHER", "COMMON",
    "GENERAL",
]

# Map any raw section to a canonical one
def normalize_section(raw):
    s = raw.upper().strip()

    # Direct match first
    if s in CANONICAL_SECTIONS:
        return s

    # Pattern matches (order matters - more specific first)
    if "PHASE" in s and "KICKOFF" in s: return "PHASE KICKOFF"
    if "PHASE" in s and "CLOSE" in s: return "PHASE CLOSE"
    if "PHASE" in s and ("PLAN" in s or "PREP" in s): return "PHASE PLANNING"
    if "GATE" in s or s in ("DECISION", "DECISIVE"): return "DECISION GATE"
    if "RETRO" in s: return "RETROSPECTIVE"

    # Job hunt specific
    if "TAKE-HOME" in s or "TAKE HOME" in s: return "INTERVIEW PREP"
    if ("FINAL" in s or "TECH" in s or "PHONE" in s) and "ROUND" in s and "PREP" in s: return "INTERVIEW PREP"
    if ("FINAL" in s or "TECH" in s or "PHONE" in s) and "ROUND" in s: return "INTERVIEW"
    if "PHONE SCREEN" in s: return "INTERVIEW"
    if "ROUND" in s and "PREP" in s: return "INTERVIEW PREP"
    if "INTERVIEW" in s and "PREP" in s: return "INTERVIEW PREP"
    if "INTERVIEW" in s: return "INTERVIEW"
    if "APPLY" in s or "APPLICATION" in s or "JOB SEARCH" in s: return "APPLY"
    if "NEGOT" in s or "PUSH-BACK" in s or "ACCEPTANCE" in s: return "NEGOTIATE"
    if "OFFER" in s: return "OFFER"
    if "ONBOARD" in s: return "ONBOARDING"
    if "COMMUNICATION CASCADE" in s: return "NETWORKING"
    if "NETWORK" in s or "OUTREACH" in s: return "NETWORKING"

    # Content
    if "OSS" in s: return "OSS"
    if "BOOTCAMP" in s or "ENCODE" in s or "OTTER" in s or "CERTIFICATION" in s: return "BOOTCAMP"
    if "FRONTEND" in s: return "FRONTEND"
    if "BLOG" in s: return "BLOG"
    if "TWITTER" in s: return "TWITTER"
    if "CONTENT" in s or "PUBLISH" in s: return "CONTENT"
    if "BRAND" in s: return "PERSONAL BRAND"
    if "ANNOUNCEMENT" in s: return "ANNOUNCEMENT"

    # Build/Deploy
    if "MAINNET" in s and "DEPLOY" in s: return "MAINNET DEPLOY"
    if "MAINNET" in s and "PROGRAM" in s: return "MAINNET DEPLOY"
    if "DEPLOY" in s: return "DEPLOY"
    if "INDEX" in s or "ANALYTICS" in s: return "INDEXING"
    if "INTEGRATION" in s and "TEST" in s: return "INTEGRATION TESTING"

    # Engineering practices
    if "TEST" in s: return "TEST"
    if "AUDIT" in s: return "AUDIT"
    if "SECUR" in s: return "SECURITY"
    if "REFACTOR" in s: return "REFACTOR"
    if "REVIEW" in s or "SOLIDIFY" in s or "STOCKTAKE" in s: return "REVIEW"
    if "POLISH" in s or "PORTFOLIO" in s: return "POLISH"
    if "DESIGN" in s: return "DESIGN"
    if "DOC" in s or "DOCUMENT" in s or "NOTE" == s: return "DOCUMENTATION"

    # Sessions / time blocks
    if "DEEP" in s and ("WORK" in s or "LEARN" in s or "DIVE" in s): return "DEEP WORK"
    if "MORNING" in s: return "MORNING SESSION"
    if "AFTERNOON" in s: return "AFTERNOON SESSION"
    if "BUFFER" in s: return "BUFFER DAY"
    if s in ("REST", "DAY OFF") or "REST DAY" in s: return "REST"
    if "LIGHT" in s and ("DAY" in s or "WORK" in s or s == "LIGHT"): return "REST"
    if "RECOVERY" in s: return "RECOVERY"

    # Learning/practice
    if "RESEARCH" in s or "RESTOCK" in s or "PRIORITIZE" in s or "CATEGORIZE" in s: return "RESEARCH"
    if "PRACTICE" in s: return "PRACTICE"
    if "RUSTLINGS" in s or "LEARN" in s or "STUDY" in s or "READ" in s or "ZK" in s: return "LEARN"

    # Build (catch-all for build-y sections)
    if "BUILD" in s or "FEAT" in s or "SCAFFOLD" in s or "IMPLEMENT" in s: return "BUILD"
    if "PROGRAM" in s or "DEMO" in s or "ORACLE" in s: return "BUILD"

    # Setup/admin
    if "SETUP" in s or "ADMIN" in s or "PIPELINE" in s or "RESTART" in s or "PRE-" in s: return "SETUP"
    if "COMMIT" in s: return "COMMIT"

    # Path / decision branching
    for p in ["PATH A", "PATH B", "PATH C"]:
        if p in s: return p
    if s == "EITHER" or s == "COMMON" or s == "ELSE" or s == "POST": return "EITHER"

    # Health
    if "HEALTH" in s or "MENTAL" in s: return "HEALTH"

    return "GENERAL"


def collect_all_sections():
    """Scan all phase files để collect every unique section name (after normalization)."""
    seen = set()
    for phase in [1, 2, 3, 4]:
        for day in parse_makeplan(phase):
            for task in parse_tasks_with_section(day["body"]):
                seen.add(normalize_section(task["section"]))
    return sorted(seen)


def create_tasks_database():
    print("→ Scanning all sections from markdown...")
    all_sections = collect_all_sections()
    print(f"  Found {len(all_sections)} unique sections")

    # Color mapping based on common keywords
    def color_for(s):
        s_low = s.lower()
        if any(k in s_low for k in ["learn", "rust", "study", "deep learn", "read"]):
            return "blue"
        if any(k in s_low for k in ["build", "feat", "implement", "develop", "scaffold"]):
            return "green"
        if any(k in s_low for k in ["test", "audit", "security", "review", "check"]):
            return "red"
        if any(k in s_low for k in ["apply", "interview", "negotiate", "offer", "phone", "tech round"]):
            return "orange"
        if any(k in s_low for k in ["network", "outreach", "personal brand", "twitter", "blog", "content"]):
            return "yellow"
        if any(k in s_low for k in ["deploy", "mainnet", "publish"]):
            return "purple"
        if any(k in s_low for k in ["onboard", "rest", "light", "buffer", "recovery", "off"]):
            return "gray"
        return "default"

    section_options = [{"name": s, "color": color_for(s)} for s in all_sections]

    print("→ Creating Daily Tasks database...")
    body = {
        "parent": {"type": "page_id", "page_id": PARENT_PAGE_ID},
        "icon": {"type": "emoji", "emoji": "✅"},
        "title": [{"type": "text", "text": {"content": "Daily Tasks"}}],
        "description": [{"type": "text", "text": {
            "content": "Tất cả tasks chia theo ngày — mỗi task 1 row có checkbox riêng. Filter theo Date/Phase/Section."
        }}],
        "is_inline": False,
        "properties": {
            "Task": {"title": {}},
            "Done": {"checkbox": {}},
            "Day": {"relation": {"database_id": DAILY_PLAN_DB, "single_property": {}}},
            "Section": {"select": {"options": section_options}},
            "Order": {"number": {"format": "number"}},
            "Date": {"date": {}},
            "Week": {"number": {"format": "number"}},
            "Phase": {
                "select": {
                    "options": [
                        {"name": "Phase 1 — Foundation", "color": "blue"},
                        {"name": "Phase 2 — Build", "color": "green"},
                        {"name": "Phase 3 — Polish + ZK", "color": "purple"},
                        {"name": "Phase 4 — Interview Circuit", "color": "orange"},
                    ]
                }
            },
        },
    }
    result = api("POST", "/databases", body)
    db_id = result["id"]
    print(f"  ✓ Created Daily Tasks DB: {db_id}")
    print(f"  ✓ Pre-populated {len(section_options)} section options")
    return db_id, set(all_sections)


def get_daily_plan_pages_by_date():
    """Query Daily Plan DB và build map {date: page_id}."""
    print("→ Building map of Daily Plan pages by date...")
    by_date = {}
    cursor = None
    while True:
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        r = api("POST", f"/databases/{DAILY_PLAN_DB}/query", body)
        for p in r["results"]:
            date_prop = p["properties"].get("Date", {}).get("date")
            if date_prop:
                by_date[date_prop["start"]] = p["id"]
        if not r.get("has_more"):
            break
        cursor = r.get("next_cursor")
    print(f"  Mapped {len(by_date)} daily pages")
    return by_date


def upload_task(tasks_db_id, day_page_id, day_info, task, valid_sections):
    """Create one task row in Daily Tasks DB."""
    week = day_info["week"]
    phase_num = get_phase_num(week)
    phase_label = PHASE_LABELS[phase_num - 1]

    section = normalize_section(task["section"])
    if section not in valid_sections:
        section = "GENERAL"

    body = {
        "parent": {"database_id": tasks_db_id},
        "properties": {
            "Task": {"title": [{"text": {"content": task["text"][:1900]}}]},
            "Done": {"checkbox": False},
            "Day": {"relation": [{"id": day_page_id}]},
            "Section": {"select": {"name": section}},
            "Order": {"number": task["order"]},
            "Date": {"date": {"start": day_info["date"]}},
            "Week": {"number": week},
            "Phase": {"select": {"name": phase_label}},
        },
    }
    api("POST", "/pages", body)


def main():
    print("=" * 60)
    print("DAILY TASKS SUB-DATABASE SETUP")
    print("=" * 60)

    # Step 1: Create Tasks DB
    tasks_db_id, valid_sections = create_tasks_database()

    # Save ID
    IDS["databases"]["daily_tasks"] = tasks_db_id
    with open(_IDS_PATH, "w") as f:
        json.dump(IDS, f, indent=2)

    # Step 2: Build date → page_id map
    pages_by_date = get_daily_plan_pages_by_date()

    # Step 3: Parse all phases và upload tasks
    print("\n→ Parsing all phase files và uploading tasks...")
    total_tasks = 0
    success = 0
    failed = []

    for phase_num in [1, 2, 3, 4]:
        days = parse_makeplan(phase_num)
        print(f"\n  Phase {phase_num}: {len(days)} days")

        for day in days:
            day_page_id = pages_by_date.get(day["date"])
            if not day_page_id:
                print(f"    [skip] No Daily Plan page for {day['date']}")
                continue

            tasks = parse_tasks_with_section(day["body"])
            for task in tasks:
                total_tasks += 1
                try:
                    upload_task(tasks_db_id, day_page_id, day, task, valid_sections)
                    success += 1
                    if success % 100 == 0:
                        print(f"    Progress: {success} tasks uploaded...")
                except Exception as e:
                    failed.append((day["date"], task["text"][:50], str(e)[:80]))
                time.sleep(0.25)

    print()
    print("=" * 60)
    print(f"DONE — {success}/{total_tasks} tasks uploaded")
    print("=" * 60)
    if failed:
        print(f"Failed: {len(failed)}")
        for d, t, e in failed[:5]:
            print(f"  {d} | {t} | {e}")


if __name__ == "__main__":
    main()
