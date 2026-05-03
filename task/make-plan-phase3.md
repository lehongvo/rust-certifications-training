<!-- ============================================================
     AGENT EXECUTION PLAN — PHASE 3: POLISH + ZK + APPLY
     Week 25–36 | 2026-11-01 → 2027-01-31
     Companion to make-plan.md (master + Phase 1)
     ============================================================ -->

# PHASE 3 — POLISH + ZK INTRO + APPLY BEGIN (W25–W36 | Nov 1, 2026 – Jan 31, 2027)

**Phase goal:** Portfolio polished, ZK skill seeded, interview circuit warmed up, real offers in pipeline.
**Success criteria for Q3 Gate (W36, Jan 22, 2027):**
- ≥ 50 applications sent total
- ≥ 5 phone screens completed
- ≥ 2 tech rounds reached
- ≥ 1 onsite/final round
- 0–1 offer (acceptable nếu market is competitive)
- ZK proof demo on mainnet
- Cross-chain demo working

**Calendar overview:**
```
M7 (Nov 2026)  W25 W26 W27 W28  — Cross-chain + Apply Tier 2-3
M8 (Dec 2026)  W29 W30 W31 W32  — ZK deeper + Apply Tier 1-2
M9 (Jan 2027)  W33 W34 W35 W36  — Real interviews + Q3 Gate
```

**Critical mindset shift in Phase 3:** Less new code, more interview prep + applications. Every project should have 2 angles: technical depth (build) AND polish (presentation).

---

## SECTION 5: PHASE 3 DAILY PLAN

### ▶ MONTH 7 (M7): Cross-Chain + Apply Begin
**Calendar:** 2026-11-01 → 2026-11-30
**Weekly Hours Target:** 15–18h (slight reduce, save energy for interviews)
**Theme:** Cross-chain bridges (Wormhole/LayerZero), aggressive applying

---

#### ◆ WEEK 25 (W25): 2026-11-02 → 2026-11-08
**Theme:** Wormhole basics + cross-chain demo design

**W25 — MONDAY 2026-11-02**

```
PHASE 3 KICKOFF (1h):
[ ] Update Notion: Phase 3 status = Active, Phase 2 = Done
[ ] Re-read rust-certification.md Section 6 (priority order)
[ ] Reflect: Phase 2 retrospective — what carries forward, what changes

LEARN (3h): WORMHOLE
[ ] Read: Wormhole protocol docs
    URL: https://docs.wormhole.com/
[ ] Topics: Guardian network, VAA (Verifiable Action Approval), token bridge
[ ] Solana-specific: Wormhole Solana SDK
    URL: https://github.com/wormhole-foundation/wormhole/tree/main/solana

COMMIT:
[ ] Commit: "docs: Phase 3 kickoff + Wormhole protocol notes"
[ ] Twitter: "Phase 3 starts: cross-chain + ZK + interview circuit. 6 months in, 6 to go. The interesting half. 🚀"
```

**W25 — TUESDAY 2026-11-03**

```
APPLY (2h): TIER 2-3 PUSH
[ ] Send 5 applications today (cumulative: 50+)
[ ] Mix:
    - 2 Solana protocols (Drift, Kamino, Marinade tier)
    - 2 hybrid Rust+EVM (1010 Trading, Caldera, Sei)
    - 1 stretch (Solana Labs / Anza if open)

LEARN (1h):
[ ] Read: LayerZero V2 docs
    URL: https://docs.layerzero.network/v2

COMMIT:
[ ] Commit: "apply: 50+ apps + LayerZero V2 notes"
```

**W25 — WEDNESDAY 2026-11-04**

```
DESIGN (3h): CROSS-CHAIN DEMO
[ ] Create projects/cross_chain_bridge/DESIGN.md
    Use case: Lock USDC on Ethereum, mint wrapped USDC on Solana
    Architecture:
    [ ] Ethereum side: Solidity contract that locks USDC + emits event
    [ ] Off-chain relayer: listens to Ethereum events, submits to Wormhole
    [ ] Solana side: Anchor program that verifies Wormhole VAA, mints wUSDC
    Use Wormhole as message layer (don't build trust assumptions yourself)
    
[ ] Note: this leverages your Solidity background (high signal for hybrid roles)

COMMIT:
[ ] Commit: "docs: cross_chain_bridge design — USDC ETH→SOL"
```

**W25 — THURSDAY 2026-11-05**

```
BUILD (3h): ETHEREUM SIDE
[ ] Create contracts/ethereum/USDCBridge.sol
    Functions:
    [ ] lock(amount, recipientOnSolana): transfers USDC in, emits Locked event
    [ ] unlock(VAA): receives messages from Solana side, releases USDC
[ ] Deploy to Goerli testnet (or Sepolia, current)
[ ] Verify on Etherscan

COMMIT:
[ ] Commit: "feat: USDCBridge Ethereum contract deployed Sepolia"
```

**W25 — FRIDAY 2026-11-06**

```
BUILD (3h): SOLANA SIDE
[ ] anchor init usdc_bridge_solana
[ ] Implement instructions:
    [ ] mint_wrapped(VAA): verify Wormhole VAA, mint wUSDC SPL token
    [ ] burn_wrapped(amount): burn wUSDC, emit Wormhole message to Ethereum
[ ] Use anchor-lang + Wormhole SDK
[ ] Test với devnet Wormhole guardian

COMMIT:
[ ] Commit: "feat: usdc_bridge_solana mint+burn với Wormhole VAA"
```

**W25 — SATURDAY 2026-11-07**

```
DEEP WORK (3h): INTEGRATION TEST CROSS-CHAIN
[ ] Setup test relayer (off-chain TypeScript script)
[ ] Test full flow:
    1. Lock 10 USDC on Sepolia → emit event
    2. Relayer picks up, submits to Wormhole guardian
    3. Generate VAA
    4. Submit VAA to Solana → mint 10 wUSDC
    5. Burn 10 wUSDC on Solana → emit event
    6. Submit to Ethereum → unlock 10 USDC
[ ] Document in README với screenshots/logs

INTERVIEW PREP (1h):
[ ] Practice explaining cross-chain flow out loud
[ ] Prepare 2-min pitch: "Why I built a bridge"

COMMIT:
[ ] Commit: "feat: cross-chain bridge full flow tested (testnet)"
```

**W25 — SUNDAY 2026-11-08**

```
[ ] W25 KPI
[ ] Twitter: bridge demo announcement với architecture diagram
[ ] REST
```

**W25 DELIVERABLES:**
```
[ ] Cross-chain bridge demo: ETH ↔ SOL via Wormhole
[ ] 50+ applications cumulative
[ ] LayerZero V2 + Wormhole knowledge
[ ] Both sides deployed (Sepolia + Solana devnet)
[ ] Full integration test passing
```

---

#### ◆ WEEK 26 (W26): 2026-11-09 → 2026-11-15
**Theme:** Bridge frontend + apply intensify + first phone screens

**W26 — MONDAY 2026-11-09**

```
BUILD (3h): BRIDGE FRONTEND
[ ] Create bridge dapp:
    [ ] Connect both Ethereum (MetaMask) + Solana (Phantom) wallets
    [ ] Lock USDC ETH → see Solana balance update
    [ ] Burn wUSDC SOL → see Ethereum balance restore
[ ] Cross-chain UX: progress steps (lock → relayer → mint, with timestamps)
[ ] Deploy frontend

COMMIT:
[ ] Commit: "feat: bridge frontend với dual wallet support"
```

**W26 — TUESDAY 2026-11-10**

```
APPLY + FOLLOW-UP (2h):
[ ] Send 5 more applications
[ ] Follow up on stale apps (10+ days)
[ ] Check: any phone screen scheduled? Confirm date/time, prep next day

INTERVIEW PREP (2h):
[ ] If interview scheduled: deep prep on company
    - Read 3 latest blog posts
    - Read team's recent commits/PRs
    - Note 3 thoughtful questions to ask interviewer

COMMIT:
[ ] Commit: "apply: 55+ + interview prep"
```

**W26 — WEDNESDAY 2026-11-11**

```
PHONE SCREEN (1h actual + prep):
If scheduled:
[ ] 30-min phone screen
[ ] Tell story: Solidity background → why Solana → projects → ZK interest
[ ] Ask about team/role
[ ] Send thank-you note within 24h

PRACTICE (3h):
[ ] LeetCode Medium x 2 in Rust
[ ] Topic: hashmap-heavy problems

COMMIT:
[ ] Commit: "interview: phone screen with [company] + practice"
```

**W26 — THURSDAY 2026-11-12**

```
LEARN (3h): SOLANA ADVANCED TOPICS
[ ] Read: Sealevel parallel runtime details
    URL: https://medium.com/solana-labs/sealevel-parallel-processing-thousands-of-smart-contracts-d814b378192
[ ] Read: Solana fee market + priority fees
[ ] These come up trong senior interviews

COMMIT:
[ ] Commit: "docs: Sealevel + fee market deep notes"
```

**W26 — FRIDAY 2026-11-13**

```
APPLY (2h):
[ ] 5 applications, focusing Tier 1 này tuần
[ ] LinkedIn outreach: connect với 3 senior engineers từ target companies

POLISH (1h):
[ ] Update CV/resume với cross-chain bridge project
[ ] Update LinkedIn projects section
[ ] Update portfolio dapp với bridge entry

COMMIT:
[ ] Commit: "polish: CV + LinkedIn + portfolio updated"
```

**W26 — SATURDAY 2026-11-14**

```
DEEP WORK (4h): MAINNET BRIDGE DEPLOY
[ ] Final security review (cross-chain has more attack surface)
[ ] Specific bridge attack vectors:
    [ ] Replay attacks (VAA reused)
    [ ] Guardian quorum attacks
    [ ] Token unlock race conditions
    [ ] Inflation via incorrect mint amount
[ ] Mitigations all in place
[ ] Deploy:
    [ ] Ethereum mainnet (cost: ~0.05 ETH gas)
    [ ] Solana mainnet (cost: ~1 SOL)
[ ] Initial test với $5 USDC bridge

COMMIT:
[ ] Commit: "deploy: bridge mainnet (4th protocol total)"
```

**W26 — SUNDAY 2026-11-15**

```
[ ] W26 KPI
[ ] Bridge mainnet announcement (Twitter + LinkedIn + Dev.to)
[ ] REST
```

**W26 DELIVERABLES:**
```
[ ] Bridge frontend deployed
[ ] Bridge mainnet on ETH + SOL (4th protocol)
[ ] 55+ applications
[ ] First phone screen completed (or soon)
[ ] Sealevel architecture knowledge
```

---

#### ◆ WEEK 27 (W27): 2026-11-16 → 2026-11-22
**Theme:** First applications conversion + content blitz

**W27 — MONDAY 2026-11-16**

```
APPLY + INTERVIEW (3h):
[ ] Send 5 applications
[ ] Track: how many phone screens have I gotten? What % conversion?
    Calculate: phone_screens / apps_sent
    Industry benchmark: 5-15% trong tốt market
[ ] If <5%: review CV/resume, ask for feedback
[ ] If >15%: scale up volume, you have signal

PRACTICE (1h):
[ ] LeetCode Medium x 1 (timed, 30 min)

COMMIT:
[ ] Commit: "apply: conversion analysis + 60+ apps"
```

**W27 — TUESDAY 2026-11-17**

```
CONTENT BLITZ (3h): TWITTER + DEV.TO + LINKEDIN
[ ] Twitter thread: "I built 4 mainnet protocols on Solana in 6 months. Here's what I learned about each."
    Tweet 1: Hook
    Tweet 2-5: One per project
    Tweet 6: Composability insight
    Tweet 7: What's next
[ ] Dev.to long-form: "Cross-Chain Bridges Demystified — A Solidity Dev's Guide"
[ ] LinkedIn post linking both

COMMIT:
[ ] Commit: "content: Phase 3 W27 blitz published"
```

**W27 — WEDNESDAY 2026-11-18**

```
INTERVIEW PREP (3h): SYSTEM DESIGN
[ ] Practice 3 system design scenarios (60 min each):
    [ ] Design a high-frequency on-chain order book
    [ ] Design an on-chain credit scoring system
    [ ] Design a cross-chain swap router
[ ] For each: account model, instruction flow, security, scaling concerns
[ ] Document your designs in /interview-prep/system-designs.md

COMMIT:
[ ] Commit: "practice: 3 system design scenarios documented"
```

**W27 — THURSDAY 2026-11-19**

```
LEARN (2h): ANCHOR INTERNALS
[ ] Read Anchor source code: anchor-lang macros
    GitHub: coral-xyz/anchor/lang/syn
[ ] Understand: how #[program], #[derive(Accounts)], #[account] generate code
[ ] Note: useful for senior interviews

PRACTICE (1h):
[ ] LeetCode Hard x 1 trong Rust
[ ] Topic: graph or DP

COMMIT:
[ ] Commit: "learn: Anchor macros internals + Hard problem"
```

**W27 — FRIDAY 2026-11-20**

```
NETWORKING (3h):
[ ] Schedule: 2 coffee chats với senior engineers (10-30 min Zoom)
[ ] Topic: ask their career path, advice for transition
[ ] Don't pitch yourself directly, build relationship
[ ] Send thank-you note với specific takeaway

COMMIT:
[ ] Commit: "network: 2 coffee chats scheduled/done"
```

**W27 — SATURDAY 2026-11-21**

```
DEEP WORK (4h): NEW BUFFER (Use this Saturday for catch-up)
[ ] Whatever's blocking: address it
    Options:
    - Catch up on missed apps
    - Refactor messy code
    - Re-read a confusing topic
    - Polish content drafts
[ ] No new features. Just polish + catchup.

COMMIT:
[ ] Commit: "polish: weekend catchup [specifics]"
```

**W27 — SUNDAY 2026-11-22**

```
[ ] W27 KPI
[ ] REST
```

**W27 DELIVERABLES:**
```
[ ] 60+ applications total
[ ] 3 system design scenarios documented
[ ] Anchor internals understood
[ ] 2 coffee chats với seniors
[ ] 1 LeetCode Hard solved
[ ] 1 Twitter thread + 1 Dev.to post + 1 LinkedIn published
```

---

#### ◆ WEEK 28 (W28): 2026-11-23 → 2026-11-29
**Theme:** Tech rounds focus + audit practice

**W28 — MONDAY 2026-11-23**

```
APPLY (2h):
[ ] 5 more applications (cumulative: 65+)

PRACTICE (2h):
[ ] LeetCode Medium x 2 (timed, 30 min each)

COMMIT:
[ ] Commit: "apply + practice cycle"
```

**W28 — TUESDAY 2026-11-24**

```
TECH ROUND PREP (3h):
If tech round scheduled:
[ ] Day-before deep prep:
    [ ] Re-read company's recent technical blog posts
    [ ] Review your own code (be ready to explain decisions)
    [ ] Prepare 5 questions to ask
    [ ] Mental rehearsal: walk through your projects in 5 min flat
    [ ] Get good sleep tonight

ELSE:
[ ] Practice mock tech round (Pramp or peer)

COMMIT:
[ ] Commit: "interview: tech round prep [company]"
```

**W28 — WEDNESDAY 2026-11-25**

```
TECH ROUND EXECUTION (1h actual):
If scheduled:
[ ] 60-90 min coding/system design round
[ ] Stay calm, think aloud, ask clarifying questions
[ ] Record what types of Q's were asked

POST-INTERVIEW (1h):
[ ] Write up: what went well, what didn't
[ ] Send thank-you note với specifics

LEARN (1h):
[ ] Bridge any gap identified during interview

COMMIT:
[ ] Commit: "interview: tech round [company] + retrospective"
```

**W28 — THURSDAY 2026-11-26**

```
AUDIT PRACTICE (3h):
[ ] Pick a recent Solana exploit (find on Twitter / Solana Daily)
[ ] Read the post-mortem
[ ] Audit the affected code yourself BEFORE reading the fix
[ ] Compare your findings vs the actual root cause
[ ] Document trong audit_practice/

COMMIT:
[ ] Commit: "practice: real-world audit case study analysis"
```

**W28 — FRIDAY 2026-11-27**

```
APPLY + NETWORK (2h):
[ ] 5 applications
[ ] Follow up on tech round status
[ ] Engage on Twitter: be visible, comment substantively

LEARN (1h):
[ ] ZK book chapter 6

COMMIT:
[ ] Commit: "apply: 70+ apps + ZK ch6"
```

**W28 — SATURDAY 2026-11-28**

```
DEEP WORK (4h): ZK PROOF DEMO V2 — MAINNET
[ ] Polish the ZK balance proof demo:
    [ ] Better UX trên frontend
    [ ] Comprehensive README explaining ZK concepts simply
    [ ] Multiple proof types: balance threshold, age verification, identity attestation
[ ] Deploy mainnet (RISC Zero verifier program)

COMMIT:
[ ] Commit: "feat: ZK demo V2 mainnet với 3 proof types"
```

**W28 — SUNDAY 2026-11-29**

```
[ ] W28 KPI
[ ] M7 retrospective
[ ] REST
```

**W28 DELIVERABLES:**
```
[ ] 70+ applications cumulative
[ ] 1+ tech round completed
[ ] ZK demo v2 mainnet
[ ] 1 audit case study documented
[ ] Mock tech round practice
```

**M7 (Nov) RETROSPECTIVE CHECKPOINT:**
```
[ ] Apps: 70+ (target was 50+, exceeded)
[ ] Phone screens: 3-5
[ ] Tech rounds: 1-2
[ ] Mainnet protocols: 4 (added bridge)
[ ] ZK demo: mainnet
[ ] Network: 25+ touchpoints
[ ] Hours: 60-72h tracked
```

---

### ▶ MONTH 8 (M8): ZK Deep + Apply Tier 1
**Calendar:** 2026-11-30 → 2026-12-31
**Weekly Hours Target:** 15h (holiday season, expect lower)
**Theme:** ZK deeper dive, push Tier 1 applications, holiday content

---

#### ◆ WEEK 29 (W29): 2026-11-30 → 2026-12-06
**Theme:** ZK book deep dive + RareSkills consideration

**W29 — MONDAY 2026-11-30**

```
LEARN (3h): ZK BOOK DEEP DIVE
[ ] RareSkills ZK Book chapters 7-10
[ ] Topics: KZG commitments, Plonkish arithmetization
[ ] Note: this is heavy math. Don't expect mastery, just exposure.

PRACTICE (1h):
[ ] LeetCode Medium x 1

COMMIT:
[ ] Commit: "learn: ZK ch7-10"
```

**W29 — TUESDAY 2026-12-01**

```
DECISION: RARESKILLS ZK COURSE?
[ ] Evaluate if budget allows ($500 USD)
[ ] Pros: structured learning, networking với serious ZK devs
[ ] Cons: time commitment 8 weeks, financial cost
[ ] If YES: register
[ ] If NO: continue self-study với free resources

LEARN (2h):
[ ] zk-learning.org modules 1-3
[ ] Watch related conference talks

COMMIT:
[ ] Commit: "decision: ZK course choice + 2h self-study"
```

**W29 — WEDNESDAY 2026-12-02**

```
APPLY TIER 1 (2h):
[ ] Specifically target Tier 1 today: Solana Labs, Anza, Jito, Helius
[ ] Polish each application heavily
[ ] Reference specific recent work (their blog/PR/release)

LEARN (1h):
[ ] ZK book ch11

COMMIT:
[ ] Commit: "apply: 5 Tier 1 + ZK ch11"
```

**W29 — THURSDAY 2026-12-03**

```
INTERVIEW PREP (3h):
[ ] Mock system design: "Design Solana validator's transaction processing pipeline"
[ ] Mock Rust round: 2 problems trong 60 min

COMMIT:
[ ] Commit: "practice: system design + Rust round mock"
```

**W29 — FRIDAY 2026-12-04**

```
LEARN (3h): RISC ZERO ADVANCED
[ ] Build custom RISC Zero guest program:
    Use case: prove a sorted array has correct min/max without revealing array
[ ] Verify on Solana

COMMIT:
[ ] Commit: "feat: RISC Zero custom guest program — array attestation"
```

**W29 — SATURDAY 2026-12-05**

```
DEEP WORK (4h): NEXT PROJECT — ZK-BACKED LENDING
[ ] Idea: extend lending_protocol để allow private credit scoring
    User submits ZK proof of "credit_score > 700"
    Lending protocol gives better rate WITHOUT seeing actual score
[ ] Design document

COMMIT:
[ ] Commit: "docs: zk-backed lending design"
```

**W29 — SUNDAY 2026-12-06**

```
[ ] W29 KPI
[ ] REST
```

**W29 DELIVERABLES:**
```
[ ] ZK book chapters 7-11 read
[ ] Custom RISC Zero guest program
[ ] 5 Tier 1 applications
[ ] zk-backed lending design doc
[ ] System design + Rust mock practice
```

---

#### ◆ WEEK 30 (W30): 2026-12-07 → 2026-12-13
**Theme:** Apply intensify + interview round 2

**W30 — MONDAY 2026-12-07**

```
APPLY DRIVE (3h):
[ ] Audit existing applications: status, follow-ups needed
[ ] Send 8 new applications today
[ ] Aggressive personalization

COMMIT:
[ ] Commit: "apply: 80+ total"
```

**W30 — TUESDAY 2026-12-08**

```
INTERVIEW (if scheduled, else practice):
[ ] Tech round 2 hoặc onsite round
[ ] Be ready to do live coding với screen share
[ ] Have production code open for context if needed

PRACTICE:
[ ] LeetCode Medium x 2

COMMIT:
[ ] Commit: "interview: round 2 [company]"
```

**W30 — WEDNESDAY 2026-12-09**

```
LEARN (3h): SOLANA SECURITY DEEP DIVE
[ ] Re-read: SlowMist Solana security best practices
[ ] Read: Recent Halborn/Ottersec audit reports (3-5)
[ ] Apply audit checklist to your own portfolio one more time

COMMIT:
[ ] Commit: "audit: portfolio re-review against latest patterns"
```

**W30 — THURSDAY 2026-12-10**

```
BUILD (3h): ZK-BACKED LENDING IMPLEMENTATION
[ ] Implement ZK credit score verifier in lending_protocol
[ ] User flow:
    1. User generates ZK proof off-chain (RISC Zero)
    2. Submits proof to lending_protocol.borrow_with_proof()
    3. Protocol verifies, gives reduced rate
[ ] Test on devnet

COMMIT:
[ ] Commit: "feat: lending + ZK credit proof integration"
```

**W30 — FRIDAY 2026-12-11**

```
NETWORKING (2h):
[ ] DM 5 hiring managers từ companies bạn interviewed at
[ ] Express continued interest, share recent work
[ ] Be respectful của their time

LEARN (1h):
[ ] ZK book ch12

COMMIT:
[ ] Commit: "network: hiring manager outreach + ZK ch12"
```

**W30 — SATURDAY 2026-12-12**

```
DEEP WORK (4h): BLOG AUDIT
[ ] Write Dev.to: "Building a ZK-Backed Lending Protocol on Solana"
    Sections:
    - Problem: privacy in DeFi credit
    - Solution architecture
    - RISC Zero guest program
    - Solana verifier integration
    - Demo + code links
[ ] Make this your "showcase post" to share trong job applications

COMMIT:
[ ] Commit: "content: ZK-lending showcase post published"
```

**W30 — SUNDAY 2026-12-13**

```
[ ] W30 KPI
[ ] REST
```

**W30 DELIVERABLES:**
```
[ ] 80+ applications
[ ] Round 2 / onsite completed (1+)
[ ] ZK-backed lending implemented (devnet)
[ ] Showcase blog post published
[ ] Hiring manager outreach 5
```

---

#### ◆ WEEK 31 (W31): 2026-12-14 → 2026-12-20
**Theme:** Holiday content + apply quietly

**W31 — MONDAY 2026-12-14**

```
HOLIDAY MODE: Many companies pause hiring last 2 weeks of Dec.
Focus: build, content, learn (apply spam is wasted)

LEARN (3h):
[ ] Spend 3h on hardest topic still confusing
[ ] Whatever it is: ownership edge cases, ZK math, Solana sealevel

COMMIT:
[ ] Commit: "learn: deep dive [hardest topic]"
```

**W31 — TUESDAY 2026-12-15**

```
PROJECT POLISH (3h):
[ ] Pick weakest project, spend 3h on polish:
    [ ] Better tests
    [ ] Better docs
    [ ] Better frontend if applicable

COMMIT:
[ ] Commit: "polish: [project] improvements"
```

**W31 — WEDNESDAY 2026-12-16**

```
LEARN (3h):
[ ] Read: 3 senior engineer career blogs (e.g., Pragmatic Engineer)
[ ] Note: how they think about career, decision making, growth

COMMIT:
[ ] Commit: "docs: senior career reading notes"
```

**W31 — THURSDAY 2026-12-17**

```
INTERVIEW PREP (3h):
[ ] Compile list of all Q's you've been asked so far
[ ] For each: write your best answer
[ ] Practice saying answers out loud (not reading)

COMMIT:
[ ] Commit: "practice: interview Q&A bank"
```

**W31 — FRIDAY 2026-12-18**

```
LIGHT APPLY (1h):
[ ] 2-3 applications only (low season, focus quality)

LEARN (2h):
[ ] ZK book ch13

COMMIT:
[ ] Commit: "apply: light + ZK ch13"
```

**W31 — SATURDAY 2026-12-19**

```
DEEP WORK (4h): YEAR-IN-REVIEW POST
[ ] Write Dev.to: "8 Months from Solidity to Solana — A Yearly Reflection"
    Sections:
    - Where I started (May 2026)
    - Phase 1, 2, 3 milestones
    - 5 protocols built (4 mainnet)
    - Numbers: commits, blog posts, applications, interviews
    - Mistakes I made
    - What I'd do differently
    - 2027 goals

COMMIT:
[ ] Commit: "content: 8-month retrospective"
```

**W31 — SUNDAY 2026-12-20**

```
[ ] W31 KPI
[ ] Publish year-in-review post (will get traction)
[ ] REST
```

**W31 DELIVERABLES:**
```
[ ] Year-in-review blog published
[ ] Project polish on weakest one
[ ] Interview Q&A bank
[ ] Hardest topic clarified
[ ] 2-3 light applications
```

---

#### ◆ WEEK 32 (W32): 2026-12-21 → 2026-12-27
**Theme:** Christmas week — REST + light learning

**W32 — MONDAY 2026-12-21**

```
LIGHT DAY (1.5h):
[ ] Read 1 article in morning
[ ] 30 min refactoring code

COMMIT:
[ ] Commit: "chore: light Monday refactor"
```

**W32 — TUESDAY 2026-12-22**

```
LIGHT DAY (1.5h):
[ ] Watch 1 conference talk (Solana Breakpoint hoặc similar)
[ ] Note 3 interesting takeaways

COMMIT:
[ ] Commit: "learn: conference talk notes"
```

**W32 — WEDNESDAY 2026-12-23**

```
LIGHT DAY (1.5h):
[ ] Read 1 chapter of programming book (anything except Rust — broaden)
    Suggestions: Designing Data-Intensive Applications, Database Internals

COMMIT:
[ ] Commit: "learn: programming book reading"
```

**W32 — THURSDAY 2026-12-24**

```
DAY OFF
Spend với family / friends. No commits today is OK.
```

**W32 — FRIDAY 2026-12-25**

```
DAY OFF
Christmas. Rest.
```

**W32 — SATURDAY 2026-12-26**

```
LIGHT DAY (2h):
[ ] Light coding: explore a new library (e.g., bevy, axum)
[ ] Just hello-world experiments

COMMIT:
[ ] Commit: "explore: [library]"
```

**W32 — SUNDAY 2026-12-27**

```
[ ] W32 KPI (light week)
[ ] Set 2027 personal goals
[ ] REST
```

**W32 DELIVERABLES:**
```
[ ] Genuine rest taken (RULE-02 holiday extension)
[ ] 2-3 light learning sessions
[ ] No code panic, no app sending
[ ] 2027 goals drafted
```

---

#### ◆ WEEK 33 (W33): 2026-12-28 → 2027-01-03
**Theme:** New Year ramp-up + apply restart

**W33 — MONDAY 2026-12-28**

```
RESTART (3h):
[ ] Review state: where am I at end of 2026?
[ ] Make 2027 plan crisp:
    - Q1: Phase 4 — Interview Circuit + Offer
    - Q2: Onboard new role
    - Q3-Q4: Plan for tier 2→3 senior trajectory
[ ] Update Notion goals

APPLY RESTART (1h):
[ ] Send 3 applications (companies are back from holidays now)

COMMIT:
[ ] Commit: "plan: 2027 plan + apply restart"
```

**W33 — TUESDAY 2026-12-29**

```
APPLY (2h):
[ ] 5 more applications (cumulative: 95+)

LEARN (1h):
[ ] ZK book ch14

COMMIT:
[ ] Commit: "apply: 95+ + ZK ch14"
```

**W33 — WEDNESDAY 2026-12-30**

```
INTERVIEW PREP (3h):
[ ] Update CV với year-end stats
[ ] Practice the year retrospective story (you'll get asked)
[ ] Refine your 30-second pitch

COMMIT:
[ ] Commit: "polish: CV + pitch refresh"
```

**W33 — THURSDAY 2026-12-31**

```
NEW YEAR'S EVE — LIGHT
[ ] 1h work max
[ ] Tag GitHub: git tag year-end-2026
[ ] Twitter: "End of 2026. Stats: [numbers]. 2027 = land the role. 🚀"

COMMIT:
[ ] Commit: "milestone: year-end-2026 tag"
```

**W33 — FRIDAY 2027-01-01**

```
NEW YEAR'S DAY — REST
Optional: 30 min review of recent applications, prep next week
```

**W33 — SATURDAY 2027-01-02**

```
DEEP WORK (4h):
[ ] Mock interview practice: full 2-hour simulation
    Structure: 10 min behavioral + 60 min coding + 50 min system design
[ ] Record yourself, review

COMMIT:
[ ] Commit: "practice: 2h full mock interview"
```

**W33 — SUNDAY 2027-01-03**

```
[ ] W33 KPI
[ ] REST
```

**W33 DELIVERABLES:**
```
[ ] 2027 plan finalized
[ ] 95+ applications cumulative
[ ] CV + pitch refreshed
[ ] Full 2-hour mock interview done
[ ] Year-end-2026 tagged
```

---

#### ◆ WEEK 34 (W34): 2027-01-04 → 2027-01-10
**Theme:** January push — companies actively hiring, push hard

**W34 — MONDAY 2027-01-04**

```
APPLY HEAVY (3h):
[ ] 8 applications today (companies restocking from January budgets)
[ ] Mix tiers: 4 Tier 1, 2 Tier 2, 2 Tier 3

COMMIT:
[ ] Commit: "apply: 100+ apps milestone"
```

**W34 — TUESDAY 2027-01-05**

```
INTERVIEW BUSY (vary):
If multiple interviews scheduled:
[ ] Manage scheduling carefully (don't double-book)
[ ] Each interview: full prep night before, day-of execution

PRACTICE (1h):
[ ] LeetCode Medium x 1

COMMIT:
[ ] Commit: "interview: [companies] + practice"
```

**W34 — WEDNESDAY 2027-01-06**

```
DEEP WORK (3h): TAKE-HOME ASSIGNMENTS
If any take-home assignments:
[ ] Devote dedicated time
[ ] Quality over speed (impress với architecture, tests, docs)
[ ] Submit early when possible

ELSE:
[ ] Build a "demo project" you can use as take-home if asked
    Idea: a small Solana program with full test suite, clean README

COMMIT:
[ ] Commit: "interview: take-home work"
```

**W34 — THURSDAY 2027-01-07**

```
INTERVIEW LOOP (variable):
Continue interview activities

PRACTICE (2h):
[ ] System design: practice 1 new scenario
[ ] LeetCode: 1 problem

COMMIT:
[ ] Commit: "practice: interview daily"
```

**W34 — FRIDAY 2027-01-08**

```
APPLY + FOLLOW UP (3h):
[ ] 5 applications
[ ] Follow-up status checks on 10+ stale apps
[ ] Polite "still interested, here's recent work" notes

COMMIT:
[ ] Commit: "apply + follow-up cycle"
```

**W34 — SATURDAY 2027-01-09**

```
DEEP WORK (4h): IF HOMEWORK PENDING
Take-home assignments take priority

ELSE:
[ ] Research: Phase 4 specific company prep
    Pick 5 most likely to convert, research deep:
    - Recent commits, technical decisions
    - Interview formats they use
    - Glassdoor/Levels.fyi data

COMMIT:
[ ] Commit: "research: Phase 4 top 5 companies deep dive"
```

**W34 — SUNDAY 2027-01-10**

```
[ ] W34 KPI
[ ] REST
```

**W34 DELIVERABLES:**
```
[ ] 110+ applications cumulative
[ ] Multiple interviews active
[ ] Take-home assignments delivered
[ ] Top 5 company deep research done
```

---

#### ◆ WEEK 35 (W35): 2027-01-11 → 2027-01-17
**Theme:** Interview circuit peak

**W35 — MONDAY 2027-01-11**

```
INTERVIEW DAY:
Likely 1-2 interviews this day. Manage energy carefully.

PRACTICE (1h):
[ ] Quick warmup problem in morning
```

**W35 — TUESDAY 2027-01-12**

```
INTERVIEW + RECOVERY:
Continue interview loop
Recovery: 30 min walk, good meal, sleep early
```

**W35 — WEDNESDAY 2027-01-13**

```
PRACTICE (3h):
[ ] After multiple interviews, identify common gaps
[ ] Spend 3h directly on weakest area
```

**W35 — THURSDAY 2027-01-14**

```
APPLY (2h):
[ ] Send 5 more applications

INTERVIEW (variable):
```

**W35 — FRIDAY 2027-01-15**

```
LEARN (3h): NEGOTIATION PREP
[ ] Read: "Negotiating" by Chris Voss (or summary)
[ ] Read: 10 minutes of Levels.fyi data for target salary range
[ ] Prepare: counter-offer template, what to say if asked salary expectations
```

**W35 — SATURDAY 2027-01-16**

```
DEEP WORK (4h): CASE STUDY PREP
Some senior interviews ask "tell me about a hard problem you solved"
[ ] Document 3 such stories trong STAR format:
    Situation: context
    Task: what was needed
    Action: what you did specifically
    Result: outcome

COMMIT:
[ ] Commit: "practice: 3 STAR stories prepared"
```

**W35 — SUNDAY 2027-01-17**

```
[ ] W35 KPI
[ ] REST
```

**W35 DELIVERABLES:**
```
[ ] Multiple interview rounds completed
[ ] Negotiation prep
[ ] STAR stories ready
[ ] 115+ applications
```

---

#### ◆ WEEK 36 (W36): 2027-01-18 → 2027-01-31
**Theme:** Q3 Decision Gate + Phase 4 prep
**Note:** W36 extended (~2 weeks) to clean close M9

**W36 — MONDAY 2027-01-18**

```
Q3 GATE EVALUATION (3h):
[ ] Run Q3 Gate checklist (see make-plan-protocols.md):
    
    GO criteria (must hit ≥ 5/8):
    [ ] 50+ applications sent (have 115+) ✓
    [ ] 5+ phone screens (verify count)
    [ ] 2+ tech rounds (verify)
    [ ] 1+ onsite/final (verify)
    [ ] 0-1 offer received
    [ ] ZK demo on mainnet
    [ ] Cross-chain demo working
    [ ] Portfolio dapp live
    
[ ] Result: GO / SLOW / NO-GO

DECISION:
[ ] If GO: Phase 4 = full interview circuit (you're on track)
[ ] If SLOW: identify bottleneck (CV? coding? specific interview type?)
[ ] If NO-GO: trigger Plan C (hackathon path - see make-plan-protocols.md)

COMMIT:
[ ] Commit: "milestone: Q3 Gate [RESULT]"
```

**W36 — TUESDAY 2027-01-19**

```
INTERVIEW + APPLY (3h):
Continue active interview loop
5 new applications to top tier

COMMIT:
[ ] Commit: "apply: ongoing"
```

**W36 — WEDNESDAY 2027-01-20**

```
PHASE 4 PLANNING (3h):
[ ] Read make-plan-phase4.md (when written)
[ ] Set Phase 4 goals trong Notion:
    - Target: 1 offer Tier 1, 2 offers Tier 2-3
    - Negotiate: > $5k/month minimum, target $7k+
    - Choose: best fit (not just highest pay)
[ ] Pre-load Phase 4 Daily Plan trong Notion

COMMIT:
[ ] Commit: "plan: Phase 4 planning"
```

**W36 — THURSDAY 2027-01-21**

```
INTERVIEW LOOP (variable):
Active rounds continue

LEARN (1h):
[ ] Compensation research: current Solana/Rust salaries Q1 2027
```

**W36 — FRIDAY 2027-01-22**

```
APPLY + INTERVIEW (variable):

NETWORKING (2h):
[ ] 3 referral conversations
[ ] Update LinkedIn với recent interviews completed (use vague language)

COMMIT:
[ ] Commit: "network: referrals + LinkedIn refresh"
```

**W36 — SATURDAY 2027-01-23**

```
DEEP WORK (4h): MENTAL HEALTH CHECK
3 months của heavy interview pressure. Pause and assess:
[ ] Am I sleeping enough?
[ ] Am I exercising at all?
[ ] Have I become irritable?
[ ] Am I eating regularly?
[ ] If yes to any: take 1 full day OFF this weekend, no exceptions
```

**W36 — SUNDAY 2027-01-24**

```
[ ] REST
```

**W36 — MONDAY 2027-01-25**

```
INTERVIEW + APPLY:
Continue active circuit
5 new applications
```

**W36 — TUESDAY 2027-01-26**

```
INTERVIEW + LEARN:
Active rounds
1h on whichever topic interviewers ask most about
```

**W36 — WEDNESDAY 2027-01-27**

```
APPLY (3h):
[ ] Last week of January push
[ ] 8 high-quality applications

COMMIT:
[ ] Commit: "apply: end-Jan push"
```

**W36 — THURSDAY 2027-01-28**

```
INTERVIEW + DOCUMENT:
Continue interviews
Document each: what was asked, what I answered, what I'd improve
```

**W36 — FRIDAY 2027-01-29**

```
PHASE 3 RETROSPECTIVE (3h):
[ ] Honest assessment of 3 months:
    [ ] Apps sent vs offers ratio
    [ ] Best/worst interview experiences
    [ ] What surprised me about the market
    [ ] What I'd tell W25-me

[ ] Update RETRO_P3.md

COMMIT:
[ ] Commit: "docs: Phase 3 retrospective"
```

**W36 — SATURDAY 2027-01-30**

```
DEEP WORK (3h):
Light. Phase 3 done, Phase 4 starts soon.
[ ] Polish anything still rough
[ ] Pre-prep for Phase 4 first week
```

**W36 — SUNDAY 2027-01-31**
> *Last day of Phase 3 — milestone tag*

```
PHASE 3 CLOSE (2h):
[ ] Tag GitHub: git tag v3.0-phase3-complete
[ ] Update karpathy-rust README with Phase 3 stats:
    - 4-5 mainnet protocols
    - ZK demo mainnet
    - 120+ applications
    - 8-12 phone screens
    - 4-6 tech rounds
    - 2-3 onsites/finals
    - 0-2 offers received
    - 13+ blog posts
[ ] Twitter: "Phase 3 done. The interview marathon part. Phase 4 = land it. 🚀"

COMMIT:
[ ] Commit: "milestone: Phase 3 complete v3.0-phase3-complete"
```

**PHASE 3 FINAL DELIVERABLES CHECKLIST:**
```
PROGRAMS:
[ ] cross_chain_bridge — mainnet (5th protocol total: AMM + Lending + Yield + Bridge + ZK demo)
[ ] zk_proof_demo v2 — mainnet với 3 proof types
[ ] zk_lending_extension — devnet (showcase composability)

CONTENT:
[ ] Dev.to: 18+ posts total
[ ] Twitter: 25+ threads
[ ] Year-end retrospective post
[ ] LinkedIn active

NETWORK:
[ ] 30+ DM/coffee chat touchpoints
[ ] 5+ referrals secured
[ ] Hiring manager outreach 10+

JOB SEARCH:
[ ] 120+ applications total
[ ] 8-12 phone screens
[ ] 4-6 tech rounds
[ ] 2-3 onsites/finals
[ ] 0-2 offers (anywhere from $0 đến full offer hand)

PREP:
[ ] 20+ LeetCode Medium in Rust
[ ] 3+ LeetCode Hard
[ ] 5+ system design scenarios
[ ] 3 mock interviews completed
[ ] 3 STAR stories ready

LEARNING:
[ ] ZK book chapters 1-14
[ ] RISC Zero advanced (custom guests)
[ ] Solana validator architecture
[ ] Sealevel internals
[ ] Anchor macro internals

HEALTH:
[ ] No major burnout (or: addressed if happened)
[ ] Mental health check-in done
[ ] Holiday rest taken (W32)
```

---

## SECTION 5 SUMMARY: PHASE 3 STATS TARGETS

By end of W36 (2027-01-31), should have:

| Metric | Target | Realistic Floor |
|---|---|---|
| Mainnet protocols | 5 | 4 |
| Total applications | 120 | 80 |
| Phone screens | 12 | 6 |
| Tech rounds | 6 | 3 |
| Onsites/finals | 3 | 1 |
| Offers received | 2 | 0 |
| Blog posts (cumulative Phase 1-3) | 18+ | 12+ |
| ZK demo mainnet | Yes | Devnet only |
| Network touchpoints | 30+ | 15+ |
| Mental health | Sustainable | 1-2 burnout episodes (recovered) |

**If at end of W36:**
- 0 offers + <3 onsites: Trigger Plan C (hackathon path) for Phase 4
- 1 offer at low salary: Negotiate hard, but don't ghost it
- 2+ offers: Phase 4 = optimize (negotiate + choose, not chase)

---

*Phase 3 file v1.0 | Aligned to make-plan-phase2.md | Sync to Notion Daily Plan DB*
