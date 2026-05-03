<!-- ============================================================
     NOTION IMPORT GUIDE — BLOCKCHAIN CAREER 2026–2027
     Companion to make-plan.md
     Purpose: Import 365-day plan vào Notion với database structure
     ============================================================ -->

# NOTION IMPORT GUIDE — 365-DAY EXECUTION PLAN

Tài liệu này mô tả cấu trúc Notion workspace để import kế hoạch 365 ngày từ `make-plan*.md`. Mục tiêu: agent có thể tự đọc Notion, mark task hoàn thành, ghi log, và bạn check tiến độ qua dashboard.

---

## SECTION 1: WORKSPACE STRUCTURE

### 1.1 Top-level pages

```
🗂  Blockchain Career 2026–2027 (root page)
    ├── 📊 Dashboard (linked database views)
    ├── 📅 Daily Plan (database — 365 entries)
    ├── 📈 Weekly Reviews (database — 52 entries)
    ├── 🎯 Phase Milestones (database — 4 entries)
    ├── 🚪 Decision Gates (database — 4 entries)
    ├── 📈 Market Pulse (database — 52 entries)
    ├── 🛠 Projects (database — 10–12 entries)
    ├── 📝 Blog/Content Pipeline (database — 30–40 entries)
    ├── 💼 Job Application Tracker (database — 50+ entries)
    └── 🧠 Learning Log (database — daily notes)
```

Workspace name đề xuất: `lehongvo — Rust Career`

---

## SECTION 2: DAILY PLAN DATABASE

Đây là database chính chứa 365 entry, mỗi ngày 1 row.

### 2.1 Database properties

| Property | Type | Description | Example |
|---|---|---|---|
| `Date` | Date | Ngày thực hiện | 2026-05-05 |
| `Day` | Formula | Tên thứ trong tuần | Monday |
| `Week` | Number | Số tuần (1–52) | 1 |
| `Phase` | Select | 1 / 2 / 3 / 4 | Phase 1 |
| `Month` | Select | M1 → M12 | M1 |
| `Theme` | Text | Chủ đề tuần | Setup + Variables |
| `Hours_Target` | Number | Giờ học target | 3 |
| `Hours_Actual` | Number | Giờ học thực tế | 2.5 |
| `Tasks` | Text (rich) | Checklist tasks (multi-line) | See template |
| `Deliverable` | Text | Output cụ thể của ngày | Rustlings 1-6 done |
| `Status` | Select | Not Started / In Progress / Done / Skipped / Rolled Over | Done |
| `Commit_Link` | URL | Git commit của ngày | github.com/... |
| `Blockers` | Text | Vấn đề gặp phải | Lifetime confusing |
| `Notes` | Text (rich) | Reflections | What I learned |
| `Mood` | Select | 1–10 (10 = great) | 8 |
| `Tags` | Multi-select | Topic tags | rust, anchor, blog |

### 2.2 Status options + colors

```
Not Started   — Gray
In Progress   — Yellow
Done          — Green
Skipped       — Red (with mandatory note in Blockers)
Rolled Over   — Orange (must update Date to new day)
```

### 2.3 Formula for `Day` property

```
formatDate(prop("Date"), "dddd")
```

### 2.4 Database views

Tạo 6 views sau:

**View 1 — Today (Default)**
- Filter: `Date = today()`
- Display: Single page card, all properties visible

**View 2 — This Week**
- Filter: `Week = current_week_number`
- Sort: Date ascending
- Display: Table

**View 3 — Calendar**
- Layout: Calendar
- Date property: `Date`
- Card title: `Theme + Status`

**View 4 — By Phase**
- Group by: `Phase`
- Sort: Date ascending
- Display: Board (Kanban)

**View 5 — Behind Schedule**
- Filter: `Status = Skipped OR Rolled Over`
- Sort: Date descending
- Purpose: Catch-up queue

**View 6 — Streak Tracker**
- Filter: `Status = Done` AND `Date >= today() - 7 days`
- Display: Gallery
- Purpose: Visual commit streak

### 2.5 Daily entry template (page content)

Mỗi row mở ra page với template sau:

```markdown
# [Date] — Week [N] Day [N] — Phase [N]

**Theme:** [from week]
**Hours target:** [X]h

## ☀️ Morning Routine (30 min)
- [ ] Đọc 1 article (Rust/Solana/Web3)
- [ ] Check Discord (5 min, no rabbit hole)
- [ ] Open tracking, review today's tasks

## 🦀 Deep Work
- [ ] [TASK 1 from make-plan]
- [ ] [TASK 2]
- [ ] [TASK 3]

## 🌙 Evening (15 min)
- [ ] Git commit + push
- [ ] Update Notion status
- [ ] 2-3 sentences in Notes

## 📊 Daily Log
**Hours:** ___
**Done:** ___
**Blocker:** ___
**Tomorrow:** ___
```

---

## SECTION 3: WEEKLY REVIEWS DATABASE

52 entries, một row per week.

### 3.1 Properties

| Property | Type | Example |
|---|---|---|
| `Week` | Number | 1 |
| `Date_Range` | Date (range) | 2026-05-02 → 2026-05-08 |
| `Phase` | Select | Phase 1 |
| `Theme` | Text | Setup + Variables |
| `Goal` | Text | Rustlings ch1-3 done |
| `Hours_Target` | Number | 15 |
| `Hours_Actual` | Number | 13.5 |
| `Commits` | Number | 5 |
| `Tasks_Done_Pct` | Number (percent) | 87 |
| `Blog_Posts` | Number | 1 |
| `Twitter_Posts` | Number | 2 |
| `Apps_Sent` | Number (Phase 3+) | 0 |
| `Interviews` | Number (Phase 4+) | 0 |
| `Mood_Avg` | Number | 7.5 |
| `Status` | Select | Done / Behind / On Track |
| `Reflection` | Text (rich) | What worked, what didn't |
| `Next_Week_Focus` | Text | Top 3 priorities |

### 3.2 Auto-fill from Daily Plan

Set up rollup property:
- `Days_Done` = count of Daily entries where Week = this week AND Status = Done
- `Hours_Sum` = sum of Hours_Actual where Week = this week
- `Mood_Avg` = average of Mood where Week = this week

---

## SECTION 4: PHASE MILESTONES DATABASE

4 entries, một row per phase.

### 4.1 Properties

| Property | Type | Example |
|---|---|---|
| `Phase` | Number | 1 |
| `Name` | Text | Foundation |
| `Date_Start` | Date | 2026-05-02 |
| `Date_End` | Date | 2026-07-31 |
| `Goal` | Text | Rust fluency + 5 Solana programs |
| `Success_Criteria` | Text | 5 deployed + tests passing |
| `Status` | Select | Locked / Active / Done |
| `Gate_Result` | Select | GO / SLOW / NO-GO |
| `Deliverables` | Relation | Linked to Projects DB |
| `Reflection` | Text (rich) | End-of-phase notes |

### 4.2 Pre-populated entries

```
Phase 1 — Foundation         | 2026-05-02 → 2026-07-31
Phase 2 — Build              | 2026-08-01 → 2026-10-31
Phase 3 — Polish + ZK + Apply | 2026-11-01 → 2027-01-31
Phase 4 — Interview Circuit  | 2027-02-01 → 2027-04-30
```

---

## SECTION 5: DECISION GATES DATABASE

4 entries, set deadline reminders.

### 5.1 Properties

| Property | Type | Example |
|---|---|---|
| `Gate` | Text | Q1 Gate |
| `Date` | Date | 2026-07-22 |
| `Phase_Closing` | Number | 1 |
| `Criteria_Checklist` | Text (rich) | See Section 8 of make-plan.md |
| `Result` | Select | Pending / GO / SLOW / NO-GO |
| `Action_Plan` | Text | If SLOW: ... |
| `Notes` | Text | Reflection |

### 5.2 Pre-populated

```
Q1 Gate — 2026-07-22 — Phase 1 → Phase 2
Q2 Gate — 2026-10-22 — Phase 2 → Phase 3
Q3 Gate — 2027-01-22 — Phase 3 → Phase 4
Final Gate — 2027-04-30 — Phase 4 evaluation
```

---

## SECTION 6: MARKET PULSE DATABASE

52 weekly entries to track market signals.

### 6.1 Properties

| Property | Type | Example |
|---|---|---|
| `Week` | Number | 1 |
| `Date` | Date | 2026-05-08 |
| `Rust_Jobs_Total` | Number | 4985 |
| `Rust_Jobs_Junior` | Number | 40 |
| `Rust_Jobs_Entry` | Number | 129 |
| `Solana_Jobs_New` | Number | 5 |
| `SOL_Price_USD` | Number | 145 |
| `Blockchain_Commits_Trend` | Select | Up / Stable / Down |
| `AI_News_Impact` | Select | Positive / Neutral / Negative |
| `Action_Required` | Checkbox | true if trigger Plan B |
| `Notes` | Text | Specifics |

### 6.2 Data sources

- web3.career/rust-jobs
- web3.career/junior+rust-jobs
- web3.career/solana-jobs
- coingecko.com (SOL price)
- electriccapital.com (developer report)

---

## SECTION 7: PROJECTS DATABASE

Track all deliverable projects (10–12 expected).

### 7.1 Properties

| Property | Type | Example |
|---|---|---|
| `Name` | Text | counter_program |
| `Type` | Select | Solana Program / Frontend / Library / Other |
| `Phase` | Number | 1 |
| `GitHub` | URL | github.com/... |
| `Devnet_ID` | Text | 7XZ... |
| `Mainnet_ID` | Text | (empty if not deployed) |
| `Tests_Passing` | Text | 6/6 |
| `Frontend_URL` | URL | vercel app |
| `Status` | Select | Not Started / In Progress / Devnet / Mainnet / Audited |
| `Description` | Text (rich) | What it does |
| `Tech_Stack` | Multi-select | Rust, Anchor, Solana, TypeScript |

### 7.2 Pre-seeded entries

```
1. wallet-cli            — Phase 1
2. solana-hello-native   — Phase 1
3. counter_program       — Phase 1
4. token_manager         — Phase 1
5. voting_program        — Phase 1
6. staking_program       — Phase 1
7. amm_program           — Phase 1
8. lending_protocol      — Phase 2 (planned)
9. yield_aggregator      — Phase 2 (planned)
10. cross_chain_bridge   — Phase 2 (planned)
11. zk_proof_demo        — Phase 3 (planned)
12. portfolio_dapp       — Phase 3 (planned)
```

---

## SECTION 8: BLOG/CONTENT PIPELINE DATABASE

Track blog posts and Twitter threads (target: 30+ pieces).

### 8.1 Properties

| Property | Type | Example |
|---|---|---|
| `Title` | Text | Week 1: What a Solidity Dev Notices |
| `Type` | Select | Blog / Thread / Long Tweet |
| `Platform` | Select | Dev.to / Twitter / LinkedIn / Hashnode |
| `Status` | Select | Idea / Draft / Edit / Published |
| `Date_Published` | Date | 2026-05-12 |
| `URL` | URL | dev.to/lehongvo/... |
| `Engagement` | Text | 50 reactions, 5 comments |
| `Linked_Project` | Relation | Projects DB |

### 8.2 Phase content cadence

```
Phase 1: 6 blog posts + 8 threads (focus: learning journey)
Phase 2: 8 blog posts + 10 threads (focus: project deep-dives)
Phase 3: 6 blog posts + 8 threads (focus: ZK intro + audits)
Phase 4: 4 blog posts + 6 threads (focus: interview lessons + retrospective)
Total: 24 posts + 32 threads = 56 pieces
```

---

## SECTION 9: JOB APPLICATION TRACKER DATABASE

Active from Phase 3 (M7 onwards), target 50+ applications.

### 9.1 Properties

| Property | Type | Example |
|---|---|---|
| `Company` | Text | Drift Protocol |
| `Role` | Text | Backend Rust Engineer |
| `Tier` | Select | Tier 1 / Tier 2 / Tier 3 |
| `Stack` | Multi-select | Rust, Solana, EVM |
| `Location` | Select | Remote / Asia / US / EU |
| `Salary_Range` | Text | $120k-$180k |
| `Source` | Select | web3.career / Direct / Referral / Telegram |
| `Status` | Select | Researched / Applied / Phone / Tech / Onsite / Offer / Rejected / Withdrew |
| `Date_Applied` | Date | 2026-09-15 |
| `Last_Contact` | Date | 2026-09-22 |
| `Contact_Person` | Text | Hiring manager name |
| `Notes` | Text (rich) | Application details, follow-ups |
| `Outcome` | Text | Offer details if any |

### 9.2 Status workflow

```
Researched → Applied → Phone Screen → Tech Round 1 → Tech Round 2 → Onsite/Final → Offer / Rejected
```

---

## SECTION 10: LEARNING LOG DATABASE

Daily quick notes (3-sentence entries).

### 10.1 Properties

| Property | Type | Example |
|---|---|---|
| `Date` | Date | 2026-05-05 |
| `Topic` | Multi-select | Ownership, PDAs, Anchor |
| `What_Learned` | Text | Ownership = no GC, RAII for resources |
| `Confused_About` | Text | Lifetime annotations syntax |
| `Question_For_Tomorrow` | Text | Why use Box<T> over Rc<T>? |
| `Linked_Day` | Relation | Daily Plan DB |

---

## SECTION 11: IMPORT WORKFLOW

Cách đưa data từ markdown vào Notion:

### 11.1 Manual setup (recommended for first time)

1. Tạo workspace mới hoặc page mới trong Notion existing workspace
2. Tạo từng database theo Section 2-10 với properties đúng
3. Setup Daily Plan database first (most data)
4. Use Notion's "Import" feature: copy each day's markdown vào page content

### 11.2 Automated (via Notion MCP)

Sau khi cài Notion MCP integration (xem `.claude/skills/notion.md`):

```
Agent prompt:
"Đọc file task/make-plan.md, parse mỗi ngày thành 1 row trong Daily Plan database.
Properties cần map:
- Date từ heading W[N] — DAY [DATE]
- Phase từ section header
- Theme từ week header  
- Tasks từ code block content (mark mỗi [ ] thành 1 todo)
- Deliverable từ phần W[N] DELIVERABLES
- Hours_Target = 3 cho weekday, 4-6 cho Saturday, 0 cho Sunday"
```

### 11.3 CSV bulk import

Generate CSV từ markdown bằng script (sẽ viết sau khi confirm structure):

```csv
Date,Day,Week,Phase,Theme,Hours_Target,Tasks,Deliverable,Status
2026-05-05,Monday,1,1,Setup + Variables,2,"Run setup checklist; Read Rust Book ch1-2",Repo seeded,Not Started
2026-05-06,Tuesday,1,1,Setup + Variables,3,"Rustlings intro1-2 variables1-6; Read ch3.1",Variables done,Not Started
...
```

Notion → Import → CSV → map columns to properties → confirm.

---

## SECTION 12: DASHBOARD SETUP

Page trang chủ với linked views từ tất cả databases:

### 12.1 Layout

```
┌─────────────────────────────────────────────────┐
│  📊 Today's Focus                                │
│  [Daily Plan view: filter Date = today]          │
│                                                  │
│  📈 This Week                                    │
│  [Weekly Reviews view: filter Week = current]    │
│                                                  │
│  🎯 Current Phase Progress                       │
│  [Progress bar from Phase Milestones]            │
│                                                  │
│  📊 Stats                                        │
│  Days completed: 45 / 365  ████░░░░░░  12%      │
│  Commits this week: 5 / 5                        │
│  Hours this week: 13.5 / 15                      │
│  Apps sent: 0 (Phase 1)                          │
│                                                  │
│  🚪 Next Decision Gate                           │
│  Q1 Gate — 2026-07-22 (in N days)                │
│                                                  │
│  📈 Market Pulse                                 │
│  Rust jobs: 4985 (▲ from 4750)                   │
│  Solana jobs: 5 new this week (▼ from 12)        │
│  Action required: NO                             │
└─────────────────────────────────────────────────┘
```

### 12.2 Key formulas

**Days completed (progress bar):**
```
slice("████████████████████░░░░░░░░░░░░░░░░░░░░░░░░",
      0, 
      round(prop("days_done") / 365 * 40))
```

**Days remaining to next gate:**
```
dateBetween(prop("Next_Gate_Date"), now(), "days")
```

---

## SECTION 13: AGENT INTEGRATION

Cách agent tương tác với Notion:

### 13.1 Daily morning routine (agent-triggered)

```
Agent prompt at 7:00 AM:
"Vào Notion, mở Daily Plan database, lấy entry có Date = today.
Đọc Tasks. Print ra checklist cho user dưới dạng:
- [Time] [Task]
- [Time] [Task]
Hỏi user: 'Sẵn sàng start ngày X không?'"
```

### 13.2 Daily evening routine (agent-triggered)

```
Agent prompt at 9:00 PM:
"Vào Notion, mở entry Daily Plan với Date = today.
Hỏi user mỗi task:
- '[Task]: done / partial / blocked?'
Update Status:
  - All done → Status = Done
  - Some partial → Status = In Progress  
  - Blocked → Status = Skipped, ask Blockers note
Set Hours_Actual based on user input.
Generate commit message từ tasks completed.
Ghi 1 dòng Reflection vào Notes."
```

### 13.3 Weekly review (every Sunday)

```
Agent prompt Sunday 8:00 PM:
"Vào Notion Weekly Reviews DB, find current week entry (or create).
Aggregate from Daily Plan DB:
  - Count days where Status = Done → fill Days_Done
  - Sum Hours_Actual → fill Hours_Sum
  - Avg Mood → fill Mood_Avg
Ask user:
  - 'What worked this week?' → fill Reflection.what_worked
  - 'What didn't?' → fill Reflection.what_didnt
  - 'Top 3 priorities for next week?' → fill Next_Week_Focus
Update Status: Done / Behind / On Track based on Tasks_Done_Pct."
```

### 13.4 Decision Gate trigger (auto)

```
Agent prompt 1 week before gate date:
"Vào Decision Gates DB, find next gate.
Run criteria checklist:
  - For each item: check evidence in Daily Plan / Projects / Apps DBs
  - Mark [x] if verified, [ ] if not
Generate report:
  - GO / SLOW / NO-GO recommendation
  - List unmet criteria
  - Suggested action plan
Notify user via Telegram/email/whatever."
```

---

## SECTION 14: FILES IN THIS PLAN SYSTEM

```
task/
├── rust-certification.md          (strategy document, 965 lines, COMMITTED)
├── make-plan.md                   (master + Phase 1 detailed, 1,895 lines)
├── make-plan-phase2.md            (Phase 2 detailed — TO CREATE)
├── make-plan-phase3.md            (Phase 3 detailed — TO CREATE)
├── make-plan-phase4.md            (Phase 4 detailed — TO CREATE)
├── make-plan-protocols.md         (Sections 7-10 — TO CREATE)
└── make-plan-notion.md            (this file — Notion integration guide)
```

---

## QUICK START CHECKLIST

```
SETUP (1 hour, do once):
[ ] Tạo Notion workspace "Rust Career"
[ ] Tạo 8 databases theo Section 2-10
[ ] Setup properties cho Daily Plan DB
[ ] Setup 6 views cho Daily Plan
[ ] Pre-populate Phase Milestones (4 entries)
[ ] Pre-populate Decision Gates (4 entries)
[ ] Setup Dashboard page với linked views
[ ] Share Notion pages với "Claude Agent" integration

DAILY (5 phút):
[ ] Mở "Today" view, xem tasks
[ ] Sau khi xong: update Status, Hours_Actual, Notes
[ ] Commit code, paste link vào Commit_Link

WEEKLY (15 phút Chủ Nhật):
[ ] Fill Weekly Review entry
[ ] Plan next week's top 3 priorities

QUARTERLY (1 giờ):
[ ] Run Decision Gate checklist
[ ] Update Phase Milestones status
```

---

*Last updated: 2026-05-02*
