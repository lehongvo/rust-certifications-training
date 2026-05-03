#!/usr/bin/env python3
"""
Setup Notion workspace cho Rust + Blockchain Career Plan 2026-2031.
Tạo 8 databases + pre-populate static data dưới parent page.

Usage:
  source .env && python3 _setup_notion.py

Output:
  _notion_ids.json — saved IDs để dùng cho subsequent operations
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error

NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
if not NOTION_API_KEY:
    print("ERROR: NOTION_API_KEY env var not set. Run: source .env")
    sys.exit(1)

PARENT_PAGE_ID = "3540a79c-06a3-814c-820d-d0373b562320"  # "Lộ trình Rust & Blockchain 2026–2031"
NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"


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
        print(e.read().decode())
        raise


# Color options for select/multi_select: default, gray, brown, orange, yellow, green, blue, purple, pink, red

# ============================================================
# DATABASE SCHEMAS
# ============================================================

DATABASES = [
    {
        "key": "daily_plan",
        "icon": "📅",
        "title": "Daily Plan",
        "description": "365-day execution plan, one row per day. Each entry has tasks, status, and deliverable.",
        "properties": {
            "Name": {"title": {}},
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
            "Month": {
                "select": {
                    "options": [{"name": f"M{i}", "color": "default"} for i in range(1, 13)]
                }
            },
            "Theme": {"rich_text": {}},
            "Hours_Target": {"number": {"format": "number"}},
            "Hours_Actual": {"number": {"format": "number"}},
            "Tasks": {"rich_text": {}},
            "Deliverable": {"rich_text": {}},
            "Status": {
                "select": {
                    "options": [
                        {"name": "Not Started", "color": "gray"},
                        {"name": "In Progress", "color": "yellow"},
                        {"name": "Done", "color": "green"},
                        {"name": "Skipped", "color": "red"},
                        {"name": "Rolled Over", "color": "orange"},
                    ]
                }
            },
            "Commit_Link": {"url": {}},
            "Blockers": {"rich_text": {}},
            "Notes": {"rich_text": {}},
            "Mood": {"number": {"format": "number"}},
            "Tags": {
                "multi_select": {
                    "options": [
                        {"name": "rust", "color": "orange"},
                        {"name": "solana", "color": "purple"},
                        {"name": "anchor", "color": "blue"},
                        {"name": "evm", "color": "green"},
                        {"name": "zk", "color": "pink"},
                        {"name": "build", "color": "yellow"},
                        {"name": "learn", "color": "blue"},
                        {"name": "blog", "color": "gray"},
                        {"name": "apply", "color": "red"},
                        {"name": "interview", "color": "orange"},
                        {"name": "network", "color": "green"},
                        {"name": "audit", "color": "brown"},
                    ]
                }
            },
        },
    },
    {
        "key": "weekly_reviews",
        "icon": "📈",
        "title": "Weekly Reviews",
        "description": "52 entries — one weekly retrospective per week. Aggregates from Daily Plan.",
        "properties": {
            "Name": {"title": {}},
            "Week": {"number": {"format": "number"}},
            "Date_Start": {"date": {}},
            "Phase": {
                "select": {
                    "options": [
                        {"name": "Phase 1", "color": "blue"},
                        {"name": "Phase 2", "color": "green"},
                        {"name": "Phase 3", "color": "purple"},
                        {"name": "Phase 4", "color": "orange"},
                    ]
                }
            },
            "Theme": {"rich_text": {}},
            "Goal": {"rich_text": {}},
            "Hours_Target": {"number": {"format": "number"}},
            "Hours_Actual": {"number": {"format": "number"}},
            "Commits": {"number": {"format": "number"}},
            "Tasks_Done_Pct": {"number": {"format": "percent"}},
            "Blog_Posts": {"number": {"format": "number"}},
            "Twitter_Posts": {"number": {"format": "number"}},
            "Apps_Sent": {"number": {"format": "number"}},
            "Interviews": {"number": {"format": "number"}},
            "Mood_Avg": {"number": {"format": "number"}},
            "Status": {
                "select": {
                    "options": [
                        {"name": "On Track", "color": "green"},
                        {"name": "Behind", "color": "red"},
                        {"name": "Slow", "color": "yellow"},
                        {"name": "Buffer Week", "color": "blue"},
                    ]
                }
            },
            "Reflection": {"rich_text": {}},
            "Next_Week_Focus": {"rich_text": {}},
        },
    },
    {
        "key": "phase_milestones",
        "icon": "🎯",
        "title": "Phase Milestones",
        "description": "4 entries — one per phase. Goals, success criteria, gate results.",
        "properties": {
            "Name": {"title": {}},
            "Phase": {"number": {"format": "number"}},
            "Date_Start": {"date": {}},
            "Date_End": {"date": {}},
            "Goal": {"rich_text": {}},
            "Success_Criteria": {"rich_text": {}},
            "Status": {
                "select": {
                    "options": [
                        {"name": "Locked", "color": "gray"},
                        {"name": "Active", "color": "yellow"},
                        {"name": "Done", "color": "green"},
                    ]
                }
            },
            "Gate_Result": {
                "select": {
                    "options": [
                        {"name": "Pending", "color": "gray"},
                        {"name": "GO", "color": "green"},
                        {"name": "SLOW", "color": "yellow"},
                        {"name": "NO-GO", "color": "red"},
                    ]
                }
            },
            "Reflection": {"rich_text": {}},
        },
    },
    {
        "key": "decision_gates",
        "icon": "🚪",
        "title": "Decision Gates",
        "description": "4 quarterly gates — formal evaluation points.",
        "properties": {
            "Name": {"title": {}},
            "Date": {"date": {}},
            "Phase_Closing": {"number": {"format": "number"}},
            "Criteria_Checklist": {"rich_text": {}},
            "Result": {
                "select": {
                    "options": [
                        {"name": "Pending", "color": "gray"},
                        {"name": "GO", "color": "green"},
                        {"name": "SLOW", "color": "yellow"},
                        {"name": "NO-GO", "color": "red"},
                    ]
                }
            },
            "Score": {"rich_text": {}},
            "Action_Plan": {"rich_text": {}},
            "Notes": {"rich_text": {}},
        },
    },
    {
        "key": "market_pulse",
        "icon": "📊",
        "title": "Market Pulse",
        "description": "52 weekly entries tracking job market signals + ecosystem health.",
        "properties": {
            "Name": {"title": {}},
            "Week": {"number": {"format": "number"}},
            "Date": {"date": {}},
            "Rust_Jobs_Total": {"number": {"format": "number"}},
            "Rust_Jobs_Junior": {"number": {"format": "number"}},
            "Rust_Jobs_Entry": {"number": {"format": "number"}},
            "Solana_Jobs_New": {"number": {"format": "number"}},
            "SOL_Price_USD": {"number": {"format": "dollar"}},
            "ETH_Price_USD": {"number": {"format": "dollar"}},
            "Trend": {
                "select": {
                    "options": [
                        {"name": "Up", "color": "green"},
                        {"name": "Stable", "color": "yellow"},
                        {"name": "Down", "color": "red"},
                    ]
                }
            },
            "AI_News_Impact": {
                "select": {
                    "options": [
                        {"name": "Positive", "color": "green"},
                        {"name": "Neutral", "color": "gray"},
                        {"name": "Negative", "color": "red"},
                    ]
                }
            },
            "Action_Required": {"checkbox": {}},
            "Notes": {"rich_text": {}},
        },
    },
    {
        "key": "projects",
        "icon": "🛠",
        "title": "Projects",
        "description": "All deliverable projects — programs, dApps, libraries.",
        "properties": {
            "Name": {"title": {}},
            "Type": {
                "select": {
                    "options": [
                        {"name": "Solana Program", "color": "purple"},
                        {"name": "EVM Contract", "color": "blue"},
                        {"name": "Frontend", "color": "green"},
                        {"name": "Library", "color": "orange"},
                        {"name": "ZK Demo", "color": "pink"},
                        {"name": "Bridge", "color": "yellow"},
                        {"name": "Other", "color": "gray"},
                    ]
                }
            },
            "Phase": {"number": {"format": "number"}},
            "GitHub": {"url": {}},
            "Devnet_ID": {"rich_text": {}},
            "Mainnet_ID": {"rich_text": {}},
            "Tests_Passing": {"rich_text": {}},
            "Frontend_URL": {"url": {}},
            "Status": {
                "select": {
                    "options": [
                        {"name": "Not Started", "color": "gray"},
                        {"name": "In Progress", "color": "yellow"},
                        {"name": "Devnet", "color": "blue"},
                        {"name": "Mainnet", "color": "green"},
                        {"name": "Audited", "color": "purple"},
                    ]
                }
            },
            "Description": {"rich_text": {}},
            "Tech_Stack": {
                "multi_select": {
                    "options": [
                        {"name": "Rust", "color": "orange"},
                        {"name": "Anchor", "color": "blue"},
                        {"name": "Solana", "color": "purple"},
                        {"name": "TypeScript", "color": "blue"},
                        {"name": "Solidity", "color": "gray"},
                        {"name": "RISC Zero", "color": "pink"},
                        {"name": "Wormhole", "color": "yellow"},
                    ]
                }
            },
        },
    },
    {
        "key": "blog_pipeline",
        "icon": "📝",
        "title": "Blog & Content Pipeline",
        "description": "Track blog posts, Twitter threads, LinkedIn posts. Target 56+ pieces over Year 1.",
        "properties": {
            "Name": {"title": {}},
            "Type": {
                "select": {
                    "options": [
                        {"name": "Blog", "color": "blue"},
                        {"name": "Thread", "color": "green"},
                        {"name": "Long Tweet", "color": "orange"},
                        {"name": "LinkedIn Post", "color": "purple"},
                    ]
                }
            },
            "Platform": {
                "select": {
                    "options": [
                        {"name": "Dev.to", "color": "blue"},
                        {"name": "Twitter", "color": "blue"},
                        {"name": "LinkedIn", "color": "blue"},
                        {"name": "Hashnode", "color": "purple"},
                        {"name": "Medium", "color": "gray"},
                    ]
                }
            },
            "Status": {
                "select": {
                    "options": [
                        {"name": "Idea", "color": "gray"},
                        {"name": "Draft", "color": "yellow"},
                        {"name": "Edit", "color": "orange"},
                        {"name": "Published", "color": "green"},
                    ]
                }
            },
            "Date_Published": {"date": {}},
            "URL": {"url": {}},
            "Engagement": {"rich_text": {}},
            "Phase": {"number": {"format": "number"}},
        },
    },
    {
        "key": "job_tracker",
        "icon": "💼",
        "title": "Job Application Tracker",
        "description": "Active from Phase 3 (M7+). Target: 200+ applications over Year 1.",
        "properties": {
            "Name": {"title": {}},
            "Company": {"rich_text": {}},
            "Role": {"rich_text": {}},
            "Tier": {
                "select": {
                    "options": [
                        {"name": "Tier 1 — Dream", "color": "purple"},
                        {"name": "Tier 2 — Strong Fit", "color": "blue"},
                        {"name": "Tier 3 — Warm-up", "color": "green"},
                    ]
                }
            },
            "Stack": {
                "multi_select": {
                    "options": [
                        {"name": "Rust", "color": "orange"},
                        {"name": "Solana", "color": "purple"},
                        {"name": "EVM", "color": "blue"},
                        {"name": "ZK", "color": "pink"},
                        {"name": "Cross-chain", "color": "yellow"},
                    ]
                }
            },
            "Location": {
                "select": {
                    "options": [
                        {"name": "Remote", "color": "green"},
                        {"name": "Asia", "color": "blue"},
                        {"name": "US", "color": "purple"},
                        {"name": "EU", "color": "orange"},
                        {"name": "Hybrid", "color": "yellow"},
                    ]
                }
            },
            "Salary_Range": {"rich_text": {}},
            "Source": {
                "select": {
                    "options": [
                        {"name": "web3.career", "color": "blue"},
                        {"name": "Direct", "color": "green"},
                        {"name": "Referral", "color": "purple"},
                        {"name": "Telegram", "color": "orange"},
                        {"name": "LinkedIn", "color": "blue"},
                        {"name": "Other", "color": "gray"},
                    ]
                }
            },
            "Status": {
                "select": {
                    "options": [
                        {"name": "Researched", "color": "gray"},
                        {"name": "Applied", "color": "blue"},
                        {"name": "Phone Screen", "color": "yellow"},
                        {"name": "Tech Round 1", "color": "yellow"},
                        {"name": "Tech Round 2", "color": "orange"},
                        {"name": "Onsite/Final", "color": "orange"},
                        {"name": "Offer", "color": "green"},
                        {"name": "Rejected", "color": "red"},
                        {"name": "Withdrew", "color": "gray"},
                        {"name": "Ghosted", "color": "gray"},
                    ]
                }
            },
            "Date_Applied": {"date": {}},
            "Last_Contact": {"date": {}},
            "Contact_Person": {"rich_text": {}},
            "Notes": {"rich_text": {}},
            "Outcome": {"rich_text": {}},
        },
    },
    {
        "key": "learning_log",
        "icon": "🧠",
        "title": "Learning Log",
        "description": "Quick daily notes — 3 sentences per entry. Topics learned, confused about, questions.",
        "properties": {
            "Name": {"title": {}},
            "Date": {"date": {}},
            "Topic": {
                "multi_select": {
                    "options": [
                        {"name": "Ownership", "color": "orange"},
                        {"name": "Lifetimes", "color": "orange"},
                        {"name": "Async/Tokio", "color": "orange"},
                        {"name": "PDAs", "color": "purple"},
                        {"name": "CPI", "color": "purple"},
                        {"name": "Anchor", "color": "blue"},
                        {"name": "SPL Tokens", "color": "purple"},
                        {"name": "Security", "color": "red"},
                        {"name": "ZK", "color": "pink"},
                        {"name": "Cross-chain", "color": "yellow"},
                        {"name": "System Design", "color": "gray"},
                    ]
                }
            },
            "What_Learned": {"rich_text": {}},
            "Confused_About": {"rich_text": {}},
            "Question_For_Tomorrow": {"rich_text": {}},
        },
    },
]


def create_database(spec):
    print(f"\n→ Creating database: {spec['icon']} {spec['title']}")
    body = {
        "parent": {"type": "page_id", "page_id": PARENT_PAGE_ID},
        "icon": {"type": "emoji", "emoji": spec["icon"]},
        "title": [{"type": "text", "text": {"content": spec["title"]}}],
        "description": [{"type": "text", "text": {"content": spec["description"]}}],
        "properties": spec["properties"],
        "is_inline": False,
    }
    result = api("POST", "/databases", body)
    db_id = result["id"]
    print(f"  ✓ Created: {db_id}")
    time.sleep(0.4)  # Rate limit safety
    return db_id


# ============================================================
# PRE-POPULATE STATIC DATA
# ============================================================

PHASE_MILESTONES = [
    {
        "Name": "Phase 1 — Foundation",
        "Phase": 1,
        "Date_Start": "2026-05-02",
        "Date_End": "2026-07-31",
        "Goal": "Rust fluency, Solana basics, 5 Anchor programs deployed devnet, daily commit streak established.",
        "Success_Criteria": "Rustlings 100%, Rust Book ch1-13 read, 5 Solana programs deployed devnet (counter, voting, token_manager, staking, AMM), 1 mainnet (counter), 6+ blog posts, 2+ OSS PRs.",
        "Status": "Active",
        "Gate_Result": "Pending",
    },
    {
        "Name": "Phase 2 — Build",
        "Phase": 2,
        "Date_Start": "2026-08-01",
        "Date_End": "2026-10-31",
        "Goal": "3 mainnet protocols (AMM, Lending, Yield Aggregator), security hardening, Encode + Otter certs, network expansion.",
        "Success_Criteria": "3+ mainnet protocols verifiable build, Encode Club Solana cert, Otter Security cert in progress, 40+ applications sent, portfolio dapp live.",
        "Status": "Locked",
        "Gate_Result": "Pending",
    },
    {
        "Name": "Phase 3 — Polish + ZK + Apply",
        "Phase": 3,
        "Date_Start": "2026-11-01",
        "Date_End": "2027-01-31",
        "Goal": "Cross-chain bridge, ZK demo on mainnet, 100+ applications, multiple interview rounds reached.",
        "Success_Criteria": "5+ mainnet protocols total, ZK demo mainnet, cross-chain working, 80+ applications, 5+ phone screens, 3+ tech rounds, 1+ onsite.",
        "Status": "Locked",
        "Gate_Result": "Pending",
    },
    {
        "Name": "Phase 4 — Interview Circuit + Offer",
        "Phase": 4,
        "Date_Start": "2027-02-01",
        "Date_End": "2027-04-30",
        "Goal": "Convert pipeline to offer ≥ $5,000/month, negotiate well, onboard successfully.",
        "Success_Criteria": "1+ offer accepted at ≥ $5k/month (target $7k+), good fit on team/tech/growth, 30+ days onboarded by Apr 30.",
        "Status": "Locked",
        "Gate_Result": "Pending",
    },
]


DECISION_GATES = [
    {
        "Name": "Q1 Gate — Phase 1 → Phase 2",
        "Date": "2026-07-22",
        "Phase_Closing": 1,
        "Criteria_Checklist": "See make-plan-protocols.md Section 8.1. 28 criteria across Rust, Solana, Projects, Quality, Brand, OSS, Health. GO ≥ 22/28 (78%+).",
        "Result": "Pending",
        "Action_Plan": "If GO: proceed Phase 2. If SLOW: catchup mode 2 weeks. If NO-GO: 1 week off + reassess timeline.",
    },
    {
        "Name": "Q2 Gate — Phase 2 → Phase 3",
        "Date": "2026-10-22",
        "Phase_Closing": 2,
        "Criteria_Checklist": "See make-plan-protocols.md Section 8.2. 22 criteria. GO ≥ 18/22 AND mainnet ≥ 2/3 AND health ≥ 2/3.",
        "Result": "Pending",
        "Action_Plan": "If GO: Phase 3 with apply begin. If SLOW: catchup W25. If NO-GO: trigger Plan B (pivot to Rust+EVM only).",
    },
    {
        "Name": "Q3 Gate — Phase 3 → Phase 4",
        "Date": "2027-01-22",
        "Phase_Closing": 3,
        "Criteria_Checklist": "See make-plan-protocols.md Section 8.3. 28 criteria. GO ≥ 22/28 AND tech rounds ≥ 3 AND health ≥ 2/3.",
        "Result": "Pending",
        "Action_Plan": "If GO: Phase 4 full interview circuit. If SLOW: identify bottleneck, fix in W37. If NO-GO: trigger Plan C (hackathon path).",
    },
    {
        "Name": "Final Gate — Year 1 Complete",
        "Date": "2027-04-30",
        "Phase_Closing": 4,
        "Criteria_Checklist": "See make-plan-protocols.md Section 8.4. 24 criteria. Primary: offer accepted ≥ $5k/month, onboarded 30+ days.",
        "Result": "Pending",
        "Action_Plan": "If GO: Year 1 success, plan Year 2 senior trajectory. If PARTIAL: address gaps in Year 2 Q1. If INCOMPLETE: extend timeline 6-12 months.",
    },
]


def populate_phase_milestones(db_id):
    print(f"\n→ Populating Phase Milestones ({len(PHASE_MILESTONES)} entries)")
    for entry in PHASE_MILESTONES:
        body = {
            "parent": {"database_id": db_id},
            "properties": {
                "Name": {"title": [{"text": {"content": entry["Name"]}}]},
                "Phase": {"number": entry["Phase"]},
                "Date_Start": {"date": {"start": entry["Date_Start"]}},
                "Date_End": {"date": {"start": entry["Date_End"]}},
                "Goal": {"rich_text": [{"text": {"content": entry["Goal"]}}]},
                "Success_Criteria": {"rich_text": [{"text": {"content": entry["Success_Criteria"]}}]},
                "Status": {"select": {"name": entry["Status"]}},
                "Gate_Result": {"select": {"name": entry["Gate_Result"]}},
            },
        }
        api("POST", "/pages", body)
        print(f"  ✓ {entry['Name']}")
        time.sleep(0.4)


def populate_decision_gates(db_id):
    print(f"\n→ Populating Decision Gates ({len(DECISION_GATES)} entries)")
    for entry in DECISION_GATES:
        body = {
            "parent": {"database_id": db_id},
            "properties": {
                "Name": {"title": [{"text": {"content": entry["Name"]}}]},
                "Date": {"date": {"start": entry["Date"]}},
                "Phase_Closing": {"number": entry["Phase_Closing"]},
                "Criteria_Checklist": {"rich_text": [{"text": {"content": entry["Criteria_Checklist"]}}]},
                "Result": {"select": {"name": entry["Result"]}},
                "Action_Plan": {"rich_text": [{"text": {"content": entry["Action_Plan"]}}]},
            },
        }
        api("POST", "/pages", body)
        print(f"  ✓ {entry['Name']}")
        time.sleep(0.4)


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("NOTION SETUP — Rust + Blockchain Career Plan 2026-2031")
    print("=" * 60)
    print(f"Parent page: {PARENT_PAGE_ID}")

    # Verify parent page accessible
    parent = api("GET", f"/pages/{PARENT_PAGE_ID}")
    print(f"Parent confirmed accessible.")

    # Create all 8 databases
    db_ids = {}
    for spec in DATABASES:
        db_id = create_database(spec)
        db_ids[spec["key"]] = db_id

    # Save IDs (next to this script, not cwd)
    from pathlib import Path
    output_file = Path(__file__).parent / ".notion_ids.json"
    with open(output_file, "w") as f:
        json.dump({
            "parent_page_id": PARENT_PAGE_ID,
            "databases": db_ids,
        }, f, indent=2)
    print(f"\n→ Saved IDs to {output_file}")

    # Pre-populate static data
    populate_phase_milestones(db_ids["phase_milestones"])
    populate_decision_gates(db_ids["decision_gates"])

    print("\n" + "=" * 60)
    print("STAGE 1 COMPLETE")
    print("=" * 60)
    print(f"\n8 databases created under: {PARENT_PAGE_ID}")
    print("Pre-populated:")
    print("  - 4 Phase Milestones")
    print("  - 4 Decision Gates")
    print("\nNext stage: bulk-import 365 daily plan entries")
    print("  Option A: continue this script với --daily flag")
    print("  Option B: export CSV và import qua Notion UI")


if __name__ == "__main__":
    main()
