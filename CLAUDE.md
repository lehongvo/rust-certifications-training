# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Rust certifications training workspace. Tasks are placed under the `task/` directory.

## Workflow Rules

Rule priority order: **karpathy-guidelines → plan_before_code → domain rules → commit_push_approval**

### Coding Discipline (Karpathy Guidelines — applied first)

1. **Think before coding** — state assumptions explicitly; ask if uncertain; present multiple interpretations instead of picking silently.
2. **Simplicity first** — minimum code that solves the problem; no speculative features, abstractions, or error handling for impossible scenarios.
3. **Surgical changes** — touch only what the task requires; match existing style; mention (don't delete) unrelated dead code; remove only imports/vars your own changes orphaned.
4. **Goal-driven execution** — define verifiable success criteria before starting; for multi-step tasks, state a brief numbered plan with a `verify:` check per step.

### Commit Rules

- **Never `git commit` without explicit user approval.** Show `git status`, a change summary, and the proposed commit message first. Wait for "ok", "commit", "go", or equivalent.
- **Never push without explicit user instruction.**

### Specialized Agents

| Agent | Trigger | Model |
|---|---|---|
| `bug-fix-workflow` | Any bug, error, crash, stack trace, failing test | opus |
| `code-review-commit-parallel` | Large commits (50+ files) needing comprehensive review | opus |

Agent institutional memory lives in `.claude/agent-memory/<agent-name>/MEMORY.md` — read before starting complex work.

## Rust Commands

Once Rust code exists under `task/`, standard commands apply:

```bash
cargo build          # compile
cargo test           # run all tests
cargo test <name>    # run a single test by name
cargo clippy         # lint
cargo fmt            # format
```
