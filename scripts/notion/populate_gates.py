#!/usr/bin/env python3
"""
Populate page bodies cho Decision Gates + Phase Milestones với to_do checkboxes.

Parses:
- task/make-plan-protocols.md Section 8 (4 Decision Gates)
- task/make-plan*.md Final Deliverables sections (4 Phase Milestones)

Result: mỗi entry có heading + to_do blocks trong page body — click để check off criteria.

Usage:
  source .env && python3 scripts/notion/populate_gates.py
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

_IDS_PATH = Path(__file__).parent / ".notion_ids.json"
with open(_IDS_PATH) as f:
    IDS = json.load(f)
GATES_DB = IDS["databases"]["decision_gates"]
PHASES_DB = IDS["databases"]["phase_milestones"]

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
        body_str = e.read().decode()[:300]
        raise Exception(f"HTTP {e.code}: {body_str}")


# ============================================================
# PARSE CRITERIA FROM MARKDOWN
# ============================================================

def parse_criteria_block(text):
    """Parse a code-block-style criteria checklist into (category_header, [tasks]) groups.

    Format expected:
        CATEGORY (must hit ≥ X/Y):
        [ ] task 1
        [ ] task 2

        ANOTHER CATEGORY:
        [ ] task 3
    """
    groups = []
    current_header = None
    current_tasks = []

    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue

        # Category header
        header_match = re.match(r'^([A-Z][A-Z\s/+\-,()0-9≥]+(?:\s*\([^)]+\))?):\s*$', stripped)
        if header_match:
            if current_header and current_tasks:
                groups.append((current_header, current_tasks))
            current_header = header_match.group(1).strip()
            current_tasks = []
            continue

        # Task
        task_match = re.match(r'^\[\s\]\s+(.+)$', stripped)
        if task_match:
            current_tasks.append(task_match.group(1).strip())

    if current_header and current_tasks:
        groups.append((current_header, current_tasks))

    return groups


def extract_decision_gate_criteria(gate_section_num):
    """Extract criteria from make-plan-protocols.md Section 8.{N}."""
    content = (TASK_DIR / "make-plan-protocols.md").read_text()

    # Find "### 8.X ..." through next "### 8.Y" or end
    pattern = rf'### 8\.{gate_section_num}\s+[^\n]+\n(.*?)(?=### 8\.\d|---\s*$|## ━)'
    m = re.search(pattern, content, re.DOTALL | re.MULTILINE)
    if not m:
        return []

    section_text = m.group(1)

    # Find "#### Criteria checklist" subsection through next "####" or end
    crit_match = re.search(
        r'####\s+Criteria checklist\s*\n(.*?)(?=####|\Z)',
        section_text, re.DOTALL
    )
    if not crit_match:
        return []

    crit_text = crit_match.group(1)

    # Extract content from code fence (```...```)
    fence_match = re.search(r'```\n(.*?)\n```', crit_text, re.DOTALL)
    if not fence_match:
        return []

    return parse_criteria_block(fence_match.group(1))


def extract_phase_deliverables(phase_num):
    """Extract Phase X Final Deliverables checklist from corresponding markdown."""
    if phase_num == 1:
        path = TASK_DIR / "make-plan.md"
        # "## ◉ PHASE 1 FINAL DELIVERABLES CHECKLIST" then code block
        pattern = r'##\s+◉\s+PHASE\s+1\s+FINAL\s+DELIVERABLES\s+CHECKLIST\s*\n+```\n(.*?)\n```'
    elif phase_num == 2:
        path = TASK_DIR / "make-plan-phase2.md"
        pattern = r'\*\*PHASE\s+2\s+FINAL\s+DELIVERABLES\s+CHECKLIST:\*\*\s*\n+```\n(.*?)\n```'
    elif phase_num == 3:
        path = TASK_DIR / "make-plan-phase3.md"
        pattern = r'\*\*PHASE\s+3\s+FINAL\s+DELIVERABLES\s+CHECKLIST:\*\*\s*\n+```\n(.*?)\n```'
    elif phase_num == 4:
        path = TASK_DIR / "make-plan-phase4.md"
        pattern = r'##\s+◉\s+FINAL\s+PHASE\s+4\s+DELIVERABLES\s+CHECKLIST.*?\n+```\n(.*?)\n```'
    else:
        return []

    content = path.read_text()
    m = re.search(pattern, content, re.DOTALL)
    if not m:
        return []
    return parse_criteria_block(m.group(1))


# ============================================================
# UPLOAD TO NOTION
# ============================================================

def groups_to_blocks(groups, intro_paragraph=None):
    """Convert [(header, [tasks])] into Notion blocks list."""
    blocks = []

    if intro_paragraph:
        blocks.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": intro_paragraph[:1900]}}]
            }
        })

    for header, tasks in groups:
        blocks.append({
            "object": "block",
            "type": "heading_3",
            "heading_3": {
                "rich_text": [{"type": "text", "text": {"content": header[:200]}}]
            }
        })
        for task in tasks:
            text = task[:1900]
            blocks.append({
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "rich_text": [{"type": "text", "text": {"content": text}}],
                    "checked": False
                }
            })
    return blocks


def get_existing_children(page_id):
    """Get current children block IDs of a page."""
    blocks = []
    cursor = None
    while True:
        path = f"/blocks/{page_id}/children?page_size=100"
        if cursor:
            path += f"&start_cursor={cursor}"
        r = api("GET", path)
        blocks.extend(r["results"])
        if not r.get("has_more"):
            break
        cursor = r.get("next_cursor")
    return blocks


def clear_page_body(page_id):
    """Delete all existing children blocks (so we can re-populate cleanly)."""
    children = get_existing_children(page_id)
    for b in children:
        api("DELETE", f"/blocks/{b['id']}")
        time.sleep(0.25)


def append_blocks(page_id, blocks):
    """Append blocks to page body. Notion limit 100 blocks per request."""
    if not blocks:
        return
    for i in range(0, len(blocks), 90):
        chunk = blocks[i:i+90]
        api("PATCH", f"/blocks/{page_id}/children", {"children": chunk})
        time.sleep(0.3)


def find_page_by_title(db_id, title_substring):
    """Find a page in a database whose title contains the substring."""
    r = api("POST", f"/databases/{db_id}/query", {"page_size": 20})
    for p in r["results"]:
        title_prop = p["properties"].get("Name", {}).get("title", [])
        title = "".join(t.get("plain_text", "") for t in title_prop)
        if title_substring.lower() in title.lower():
            return p["id"], title
    return None, None


# ============================================================
# MAIN
# ============================================================

DECISION_GATES = [
    (1, "Q1 Gate", "Run at end of Phase 1 (W12 — 2026-07-22). GO criteria: ≥ 22/28 (78%+) AND no category < 50%."),
    (2, "Q2 Gate", "Run at end of Phase 2 (W24 — 2026-10-22). GO criteria: ≥ 18/22 (82%+) AND mainnet ≥ 2/3 AND health ≥ 2/3."),
    (3, "Q3 Gate", "Run at end of Phase 3 (W36 — 2027-01-22). GO criteria: ≥ 22/28 (78%+) AND tech rounds ≥ 3 AND health ≥ 2/3."),
    (4, "Final Gate", "Run at end of Phase 4 (W48 — 2027-04-30). GO if primary goals ALL hit AND ≥ 19/24 (79%+)."),
]

PHASE_MILESTONES = [
    (1, "Phase 1", "Success criteria for Phase 1 — Foundation (W1-W12, May 2 → Jul 31, 2026)."),
    (2, "Phase 2", "Success criteria for Phase 2 — Build (W13-W24, Aug 1 → Oct 31, 2026)."),
    (3, "Phase 3", "Success criteria for Phase 3 — Polish + ZK + Apply (W25-W36, Nov 1, 2026 → Jan 31, 2027)."),
    (4, "Phase 4", "Success criteria for Phase 4 — Interview Circuit + Offer (W37-W48, Feb 1 → Apr 30, 2027)."),
]


def main():
    print("=" * 60)
    print("POPULATE GATES + MILESTONES WITH CHECKBOX CRITERIA")
    print("=" * 60)

    # === Decision Gates ===
    print("\n→ Processing Decision Gates...")
    for section_num, search_title, intro in DECISION_GATES:
        print(f"\n  [{search_title}]")
        page_id, found_title = find_page_by_title(GATES_DB, search_title)
        if not page_id:
            print(f"    ✗ Page not found in DB")
            continue
        print(f"    Found: {found_title} ({page_id})")

        groups = extract_decision_gate_criteria(section_num)
        if not groups:
            print(f"    ✗ No criteria parsed from markdown")
            continue
        total = sum(len(t) for _, t in groups)
        print(f"    Parsed: {len(groups)} categories, {total} criteria")

        print(f"    Clearing existing body...")
        clear_page_body(page_id)

        print(f"    Appending {total} checkboxes + {len(groups)} headers...")
        blocks = groups_to_blocks(groups, intro_paragraph=intro)
        append_blocks(page_id, blocks)
        print(f"    ✓ Done")

    # === Phase Milestones ===
    print("\n\n→ Processing Phase Milestones...")
    for phase_num, search_title, intro in PHASE_MILESTONES:
        print(f"\n  [{search_title}]")
        page_id, found_title = find_page_by_title(PHASES_DB, search_title)
        if not page_id:
            print(f"    ✗ Page not found in DB")
            continue
        print(f"    Found: {found_title} ({page_id})")

        groups = extract_phase_deliverables(phase_num)
        if not groups:
            print(f"    ✗ No deliverables parsed from markdown")
            continue
        total = sum(len(t) for _, t in groups)
        print(f"    Parsed: {len(groups)} categories, {total} deliverables")

        print(f"    Clearing existing body...")
        clear_page_body(page_id)

        print(f"    Appending {total} checkboxes + {len(groups)} headers...")
        blocks = groups_to_blocks(groups, intro_paragraph=intro)
        append_blocks(page_id, blocks)
        print(f"    ✓ Done")

    print("\n" + "=" * 60)
    print("COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
