# Notion Setup Scripts

Helper scripts for syncing the career plan from `task/make-plan*.md` to Notion.

## Files

| File | Purpose |
|---|---|
| `setup_notion.py` | Create the 9 base databases (Daily Plan, Weekly Reviews, Phase Milestones, Decision Gates, Market Pulse, Projects, Blog Pipeline, Job Tracker, Learning Log) + populate Phase Milestones + Decision Gates entries |
| `upload_daily.py` | Parse markdown phase files and upload Daily Plan rows. Each row has `to_do` blocks in page body. |
| `setup_tasks_db.py` | Create the Daily Tasks sub-database and upload all 1,891 individual task rows with `Done` checkbox + relation to Daily Plan |
| `test_parse.py` | Debug helper — prints parsed blocks for one day without uploading |
| `.notion_ids.json` | Saved DB IDs (gitignored, lives next to the scripts) |

## Prerequisites

- `.env` at repo root with `NOTION_API_KEY` set
- The Notion integration "Claude Agent" must have access to the parent page  
  (Page ID: `3540a79c-06a3-814c-820d-d0373b562320` — "Lộ trình Rust & Blockchain 2026–2031")

## Usage

All scripts read `NOTION_API_KEY` from the environment, so source `.env` first:

```bash
cd /Users/vincent/rust-certifications-training
set -a && source .env && set +a
```

### First-time setup (already done — don't re-run)

```bash
python3 scripts/notion/setup_notion.py        # Stage 1: create base 9 DBs
python3 scripts/notion/upload_daily.py --all  # Upload 353 Daily Plan rows
python3 scripts/notion/setup_tasks_db.py      # Create Daily Tasks DB + upload 1,891 task rows
```

### Re-upload a specific week (after editing markdown)

```bash
python3 scripts/notion/upload_daily.py --week 5      # only W5
python3 scripts/notion/upload_daily.py --weeks 5-8   # W5 through W8
python3 scripts/notion/upload_daily.py --all         # all 48 weeks
```

Note: re-uploading creates duplicates if the original entries still exist. Archive the old ones first if needed.

### Debug parser without uploading

```bash
python3 scripts/notion/test_parse.py
```

## Source markdown files (parsed by these scripts)

```
task/make-plan.md           # Phase 1, W1-W12
task/make-plan-phase2.md    # Phase 2, W13-W24
task/make-plan-phase3.md    # Phase 3, W25-W36
task/make-plan-phase4.md    # Phase 4, W37-W48
```

## Notes for re-running

- Scripts can run from any working directory (they resolve `.notion_ids.json` relative to themselves).
- API rate limit handled with 0.25–0.4s sleep between calls. Full Daily Tasks upload (~1,900 rows) takes ~10 minutes.
- 504 Gateway Timeouts from Notion are transient — re-run failed weeks individually with `--week N`.

## When to re-run

- Edit a daily entry in markdown → archive old Notion row + run `upload_daily.py --week N`
- Add new section options to Daily Tasks DB → manual update in Notion (script doesn't auto-add)
- Reset Notion entirely → archive all rows in each DB, then re-run all 3 setup scripts
