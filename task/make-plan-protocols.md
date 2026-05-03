<!-- ============================================================
     AGENT EXECUTION PLAN — PROTOCOLS (Sections 7–10)
     Companion to make-plan.md
     Contains: Monthly reviews, Decision Gates, Market Pulse, Emergency
     ============================================================ -->

# PROTOCOLS — Sections 7-10 (Reviews, Gates, Market, Emergency)

This file contains operational protocols referenced throughout `make-plan*.md`. Reuse mỗi tháng (Section 7), each quarter (Section 8), each week (Section 9), and when emergency triggered (Section 10).

---

## ━━━ SECTION 7: MONTHLY REVIEW TEMPLATE ━━━

Run last day của each month. Updates Notion Weekly Reviews DB rollup row hoặc creates Monthly Review entry.

### 7.1 Quantitative metrics

```yaml
month: M[N]
period: YYYY-MM-DD → YYYY-MM-DD
phase: [1/2/3/4]

hours_invested:
  target: 60-80h (15-20h/week × 4 weeks)
  actual: ___
  vs_target_pct: ___

commits:
  total: ___
  weekday_streak_pct: ___ (target 80%+)

tasks_completed:
  total_planned: ___
  completed: ___
  pct: ___

deliverables:
  programs_built: ___
  programs_devnet_deployed: ___
  programs_mainnet_deployed: ___
  tests_added: ___

content:
  blog_posts: ___ (target 1-2/month in P1-2, 0-1/month in P3-4)
  twitter_threads: ___ (target 2-3/month)
  linkedin_posts: ___ (target 1-2/month)

network:
  dms_sent: ___
  responses_received: ___
  coffee_chats: ___
  oss_prs_submitted: ___

job_search (Phase 3+):
  applications_sent_this_month: ___
  applications_cumulative: ___
  phone_screens_this_month: ___
  tech_rounds_this_month: ___
  onsites_this_month: ___
  offers_this_month: ___

learning:
  rust_book_chapters: ___ (Phase 1)
  rustlings_done: ___ (Phase 1)
  zk_book_chapters: ___ (Phase 2-3)
  audit_courses_progress: ___

health:
  burnout_episodes: ___ (target: 0)
  mood_avg: ___ (1-10, target 6+)
  exercise_days: ___ (target 12+)
  sleep_avg: ___ (target 7+ hours)
```

### 7.2 Qualitative reflection

Answer 5 questions. Be honest, not aspirational.

**1. What worked well this month?**
[3-5 specific things, not generic]

**2. What didn't work?**
[3-5 specific gaps or failures]

**3. What did I learn that surprised me?**
[Technical, market, or personal insight]

**4. What's the #1 priority for next month?**
[1 sentence, sharp]

**5. Health/sustainability check:**
[Am I able to keep this pace? Yes/No/At risk + why]

### 7.3 Decision matrix

Based on quantitative + qualitative review:

| Status | Definition | Action |
|---|---|---|
| **On Track** | Hit ≥ 75% of targets, mood ≥ 6, no major gaps | Continue current plan |
| **Slow** | Hit 50-74%, mood 5-6, 1-2 gaps | Cut scope: drop lowest priority items, extend timelines 2-4 weeks |
| **Behind** | Hit < 50%, mood < 5, 3+ gaps | Major intervention: rest week, reassess plan, maybe change phase strategy |
| **Over-extended** | Hit 100%+ but mood < 5 | Slow down deliberately, prevent burnout |

### 7.4 Output: write monthly retro file

Create `RETRO_M[N].md` trong repo với the above filled in.

Commit message: `docs: M[N] retrospective + status assessment`

### 7.5 Trigger checks

After monthly review, check:

- [ ] Trigger Decision Gate review? (Yes if at end of M3, M6, M9, M12)
- [ ] Trigger Plan B? (See Section 10.1 conditions)
- [ ] Trigger Plan C? (See Section 10.2 conditions)
- [ ] Need to update Notion Phase Milestones status?

---

## ━━━ SECTION 8: DECISION GATES ━━━

Four formal evaluation points. Run at end of each phase. Updates Notion Decision Gates DB.

### 8.1 Q1 GATE — End of Phase 1

**Date:** 2026-07-22 (end of W12 ish)
**Phase closing:** Phase 1 (Foundation)
**Phase opening (if GO):** Phase 2 (Build)

#### Criteria checklist

```
RUST FUNDAMENTALS (must hit ≥ 4/5):
[ ] Rustlings: 100% complete
[ ] Rust Book chapters 1-13 read và understood
[ ] Ownership/borrowing: explained in own words trong LEARNING_LOG
[ ] async/await with tokio: working code in projects
[ ] Generics + traits: used trong real code

SOLANA SKILLS (must hit ≥ 4/5):
[ ] First native Solana program deployed devnet
[ ] First Anchor program deployed devnet
[ ] PDA understanding: derived correctly và used trong projects
[ ] CPI executed: cross-program invocation working
[ ] Token program (SPL) understood: minting + transferring tested

PROJECTS (must hit ≥ 3/4):
[ ] counter_program — works, tested
[ ] token_manager — SPL operations working
[ ] voting_program — double-vote-proof
[ ] staking_program — interest accruing

QUALITY (must hit ≥ 3/4):
[ ] All projects have README
[ ] All projects have tests passing
[ ] No clippy warnings
[ ] LEARNING_LOG entries trong every week

PERSONAL BRAND (must hit ≥ 2/3):
[ ] Dev.to: 4+ posts published
[ ] Twitter: 6+ posts/threads
[ ] GitHub: profile README polished

OSS (must hit ≥ 1/2):
[ ] 1 PR submitted (any size)
[ ] 1 PR merged

HEALTH (must hit ≥ 2/3):
[ ] Burnout episodes: 0 OR recovered
[ ] Commit streak: ≥ 70% weekdays
[ ] Mood average: ≥ 5/10
```

#### Decision logic

```
Total checkboxes hit: ___ / 28

GO criteria: ≥ 22/28 (78%+) AND no category < 50%
SLOW criteria: 16-21/28 (57-77%)
NO-GO criteria: < 16/28 (< 57%) OR category < 50%
```

#### Actions per result

**GO:**
- Proceed to Phase 2 confidently
- No major plan changes needed
- Optionally: add 1 stretch goal for Phase 2

**SLOW:**
- Identify specifically which categories underperformed
- Phase 2 first 2 weeks: catch-up mode (no new projects, only finish backlog)
- Then resume normal Phase 2 plan
- Reduce Phase 2 scope: drop 1 of 3 mainnet protocols if needed

**NO-GO:**
- Take 1 week complete OFF (real rest)
- Review honestly: is this plan realistic given my time/energy?
- Options:
  - (a) Extend Phase 1 by 4-6 weeks, then resume
  - (b) Reduce future scope significantly (1 mainnet only by month 12)
  - (c) Trigger Plan B early (pivot to hybrid Rust+EVM only)
- Reach out to mentor/community for outside perspective

---

### 8.2 Q2 GATE — End of Phase 2

**Date:** 2026-10-22 (end of W24)
**Phase closing:** Phase 2 (Build)
**Phase opening (if GO):** Phase 3 (Polish + ZK + Apply)

#### Criteria checklist

```
MAINNET PROTOCOLS (must hit ≥ 2/3):
[ ] AMM on mainnet với verifiable build
[ ] Lending on mainnet với verifiable build
[ ] Yield aggregator on mainnet (or another protocol)

CODE QUALITY (must hit ≥ 4/5):
[ ] All mainnet programs: 80%+ test coverage
[ ] All have SECURITY.md với audit notes
[ ] All have architecture diagrams
[ ] All have production-quality READMEs
[ ] OSS PR substantive (not trivial typo) submitted

CERTIFICATIONS (must hit ≥ 2/2):
[ ] Encode Club Solana cert
[ ] Otter Security Audit cert (or in progress with > 50%)

PERSONAL BRAND (must hit ≥ 3/4):
[ ] Dev.to: 10+ cumulative posts
[ ] Twitter: 15+ threads cumulative
[ ] LinkedIn: active, optimized
[ ] Portfolio dapp deployed

NETWORK (must hit ≥ 2/3):
[ ] 10+ DMs/coffee chats senior engineers
[ ] 5+ Discord/Twitter active engagements
[ ] 2+ referral asks made

JOB SEARCH PREP (must hit ≥ 2/3):
[ ] CV updated với projects, certs, OSS
[ ] LinkedIn updated, projects pinned
[ ] 30-company target list active

HEALTH (must hit ≥ 2/3):
[ ] No major burnout episode (1 minor + recovered = OK)
[ ] Buffer week observed (W19 or similar)
[ ] Mood average ≥ 5/10
```

#### Decision logic

```
Total checkboxes hit: ___ / 22

GO criteria: ≥ 18/22 (82%+) AND mainnet ≥ 2/3 AND health ≥ 2/3
SLOW criteria: 13-17/22 (60-81%)
NO-GO criteria: < 13/22 (< 60%) OR mainnet < 2/3
```

#### Actions per result

**GO:**
- Phase 3 starts confidently
- Begin applications immediately
- Push interview prep aggressively

**SLOW:**
- Phase 3 W25 = catchup week (finish 1 missing mainnet, fix README gaps)
- Then proceed Phase 3 plan
- Reduce Phase 3 ZK ambitions if behind on protocols

**NO-GO:**
- Significant reassessment needed
- Top trigger: did the market change? (Use Section 9 data)
- If market is stable: extend Phase 2 by 6-8 weeks, push offer timeline to month 14-15
- If market deteriorated: trigger Plan B (pivot to Rust+EVM only)

---

### 8.3 Q3 GATE — End of Phase 3

**Date:** 2027-01-22 (end of W36)
**Phase closing:** Phase 3 (Polish + ZK + Apply Begin)
**Phase opening (if GO):** Phase 4 (Interview Circuit + Offer)

#### Criteria checklist

```
JOB PIPELINE (must hit ≥ 4/5):
[ ] Applications cumulative ≥ 80
[ ] Phone screens completed ≥ 5
[ ] Tech rounds ≥ 3
[ ] Onsites/finals ≥ 1
[ ] Offers received ≥ 0 (genuine OK to be 0 here)

PROTOCOL PORTFOLIO (must hit ≥ 4/5):
[ ] 4+ mainnet protocols total
[ ] ZK demo deployed (devnet OK, mainnet better)
[ ] Cross-chain demo working
[ ] Portfolio dapp showcasing all
[ ] At least 1 protocol used by external users (any small number)

INTERVIEW PREP (must hit ≥ 4/5):
[ ] 15+ LeetCode Medium in Rust
[ ] 2+ LeetCode Hard
[ ] 5+ system designs documented
[ ] 3+ STAR stories ready
[ ] 2+ mock interviews completed

CONTENT (must hit ≥ 3/4):
[ ] Dev.to: 18+ cumulative
[ ] Twitter: 25+ threads
[ ] Year-end retrospective published
[ ] At least 1 viral post (10k+ views OR clear engagement)

NETWORK (must hit ≥ 3/4):
[ ] 20+ active relationships established
[ ] 3+ referrals received
[ ] Recognized trong Solana/Rust dev Twitter (some interactions)
[ ] Notion job tracker actively maintained

LEARNING (must hit ≥ 3/4):
[ ] ZK book chapters 1-14 read
[ ] RISC Zero advanced (custom guests built)
[ ] Solana validator architecture knowledge
[ ] Otter Security audit course completed

HEALTH (must hit ≥ 2/3):
[ ] Mental health: sustainable
[ ] Holiday rest taken (W31-W32)
[ ] Mood average ≥ 5/10 (interview pressure ok to drop)
```

#### Decision logic

```
Total checkboxes hit: ___ / 28

GO criteria: ≥ 22/28 (78%+) AND tech rounds ≥ 3 AND health ≥ 2/3
SLOW criteria: 16-21/28 (57-77%)
NO-GO criteria: < 16/28 (< 57%) OR onsites = 0 with applications > 50
```

#### Actions per result

**GO:**
- Phase 4 = full interview circuit
- Push for multiple offers
- Use leverage to negotiate

**SLOW:**
- Identify bottleneck: is it CV? Coding? Specific interview type?
- Spend Phase 4 W37 fixing top bottleneck
- Continue at slightly extended timeline (offer expected month 14-15)

**NO-GO:**
- Pipeline isn't converting → strategic reset needed
- Options:
  - (a) Drastically improve CV/portfolio: 4-6 weeks polish
  - (b) Pivot focus: Solana → Rust+EVM only (less competition)
  - (c) Activate Plan C — hackathon path
  - (d) Accept lower-tier gigs as bridge income, slower path
- Get 3 senior engineer reviews of CV/portfolio
- Mock interview với someone from target company

---

### 8.4 FINAL GATE — End of Year 1

**Date:** 2027-04-30 (end of W48)
**Phase closing:** Phase 4 (Interview Circuit + Offer)
**Phase opening:** Year 2 plan

#### Criteria checklist

```
PRIMARY GOAL (must hit ALL):
[ ] Offer accepted ≥ $5,000/month
[ ] Currently in role for 30+ days
[ ] Onboarding successful (no PIP, manager satisfied)

CULTURAL FIT (must hit ≥ 3/4):
[ ] Manager and team relationships positive
[ ] Tech stack matches expectations
[ ] Growth trajectory clear
[ ] Compensation matches market

SKILLS (must hit ≥ 4/5):
[ ] Production Rust capability demonstrated trong role
[ ] Solana knowledge applied
[ ] AI fluency: using AI tools effectively trong daily work
[ ] System design skills sufficient for role
[ ] Communication and collaboration good

PORTFOLIO (durable, for future):
[ ] 5+ mainnet protocols still online
[ ] All open-source và public
[ ] Documented well
[ ] Portfolio dapp live

YEAR 2 PLAN (must hit ALL):
[ ] Year 2 themes drafted
[ ] Specific Q1 goals at new role
[ ] Continued learning plan (ZK, advanced topics)

PERSONAL (must hit ≥ 4/5):
[ ] Health intact
[ ] Financial improvement vs starting point
[ ] Confidence significantly higher
[ ] Skills top 25-30% globally trong Solana/Rust
[ ] Sustainable trajectory
```

#### Decision logic

```
Total: ___ / 24

GO (Year 1 success): ≥ 19/24 (79%+) AND primary goals ALL hit
PARTIAL: hit primary goals nhưng < 19/24 (still success, less polish)
INCOMPLETE: missed primary goals (offer not accepted yet)
```

#### Actions per result

**GO:**
- Year 1 complete. Celebrate.
- Year 2: focus on senior trajectory, deeper specialization
- Annual review: do this exercise again next May

**PARTIAL:**
- Year 1 mostly done. Identify what's missing.
- Address gaps trong Q1 of Year 2 alongside new role

**INCOMPLETE:**
- Don't panic. Many devs take 18-24 months.
- Reassess: was the timeline too aggressive?
- Continue applying while taking bridge income
- Plan extended timeline: Year 2 = "completion year"

---

## ━━━ SECTION 9: MARKET PULSE TRACKER ━━━

Run weekly (every Sunday). Updates Notion Market Pulse DB.

### 9.1 What to track

```yaml
week: W[N]
date: YYYY-MM-DD

job_market:
  rust_jobs_total_web3_career: ___
    source: https://web3.career/rust-jobs
  rust_jobs_junior: ___
    source: https://web3.career/junior+rust-jobs
  rust_jobs_entry: ___
    source: https://web3.career/entry-level+rust-jobs
  solana_jobs_new_this_week: ___
    source: https://web3.career/solana-jobs
  remote_rust_jobs: ___
    source: https://web3.career/remote+rust-jobs

market_signals:
  sol_price_usd: ___
    source: https://www.coingecko.com/en/coins/solana
  eth_price_usd: ___
  btc_price_usd: ___

ecosystem_signals:
  notable_solana_news: ___
    [3-5 bullet points: launches, hacks, regulation, etc.]
  notable_rust_news: ___
    [Microsoft, Google, AWS adoption news]
  notable_ai_news: ___
    [GPT/Claude/etc. milestones affecting dev]

talent_flow:
  high_profile_hires: ___
    [Senior eng joining/leaving major protocols]
  layoffs: ___
    [Major Web3 layoffs announced]

competitor_signals:
  hackathons_open: ___
    [List of open hackathons]
  hiring_trends: ___
    [Companies actively hiring vs frozen]
```

### 9.2 Weekly assessment

Answer 3 questions:

**1. Is the market healthier or weaker than last week?**
- Healthier: more jobs posted, fewer layoffs, positive news
- Weaker: jobs dropping, layoffs, negative news
- Stable: similar

**2. Does my plan need adjustment?**
- If healthier: continue or accelerate
- If weaker for 4+ weeks: trigger Plan B consideration
- If stable: continue

**3. Are there opportunities I missed this week?**
- Hackathon registration deadline?
- Specific company hiring announcement?
- Conference talk worth attending?

### 9.3 Trigger conditions

If ANY of these conditions are true for 4+ consecutive weeks, trigger Plan B (Section 10.1):

- Solana new jobs trên web3.career: < 3/week (vs typical 5-10)
- SOL price < $80 sustained
- Major Solana protocol layoff announced
- Class action lawsuit escalation (Pump.fun, Solana Labs, Foundation)

If ANY of these are true, trigger Plan C (Section 10.2):

- Total Rust Web3 jobs drop > 30% from baseline 4,985
- Major AI capability leap (e.g., AI auto-builds full DeFi protocols)
- 3+ major DeFi exploits trong 1 month (kill ecosystem trust)

### 9.4 Output

Create weekly entry trong Notion Market Pulse DB.

Commit (in personal repo, optional): `docs: market pulse W[N] — [brief signal]`

---

## ━━━ SECTION 10: EMERGENCY PROTOCOLS ━━━

Activated only when triggers in Section 9.3 are hit hoặc Decision Gates indicate NO-GO.

### 10.1 PLAN B: Pivot to Rust + EVM Only

**Trigger conditions:**
- Solana market cooling: 4+ weeks of weak signals (Section 9.3)
- Q2 Gate result = NO-GO
- Personal preference shift after Phase 2

**What changes:**

```
SCOPE REDUCTION:
Drop:
[ ] Solana-only project ambitions trong Phase 3-4
[ ] ZK on Solana focus (shift to ZK on EVM if any)
[ ] Solana-specific job applications

ADD/STRENGTHEN:
[ ] Rust + EVM roles primary target
[ ] Foundry/Hardhat re-skill (you already know basics)
[ ] L2 expertise (Optimism, Base, Arbitrum)
[ ] MEV-related infrastructure (you know EVM internals)

PORTFOLIO ADJUSTMENT:
Existing Solana protocols stay (don't delete, just don't promote)
Add:
[ ] 1 Rust + EVM project (e.g., Foundry plugin, MEV bot, L2 indexer)
[ ] Rust on EVM L2 example
[ ] Cross-chain bridge with EVM focus

TARGET COMPANIES (Plan B priority list):
- 1010 Trading (Rust + EVM systems)
- Caldera (rollup infrastructure)
- Sei Foundation (Rust + EVM hybrid)
- Hyperliquid (Rust DEX, but in-person Singapore)
- Ondo Finance
- Polymarket (heavy Rust + EVM)
- Drift (Solana, but uses EVM-like patterns)
- Karak Network
- LayerZero, Wormhole (cross-chain)
- Eigen Labs / EigenLayer (EVM L2 infrastructure)

TIMELINE:
Plan B may add 1-2 months because retooling
Realistic: month 14-16 instead of 12
```

**Plan B execution checklist:**

```
[ ] Document Plan B activation reason trong RETRO_PIVOT.md
[ ] Update Notion Phase Milestones: pivot tagged
[ ] Notify mentors/network: "I'm shifting focus to Rust + EVM hybrid"
[ ] Refresh CV: emphasize EVM strength + Rust learning
[ ] Update LinkedIn: same
[ ] Pause some Solana applications (unless really good fit)
[ ] Begin learning EVM tools you've forgotten
[ ] First Rust + EVM project: 4-6 weeks, can be relatively small
[ ] Re-enter applications strongly month later
```

---

### 10.2 PLAN C: Hackathon Path

**Trigger conditions:**
- Q3 Gate result = NO-GO with apps > 80 and offers = 0
- Plan B also failed (3+ months no traction)
- Major market collapse (Section 9.3 Plan C triggers)
- Personal: enjoying building > job hunting

**What changes:**

```
PIVOT FROM JOB HUNT TO BUILDER PATH:

PRIMARY ACTIVITY:
[ ] Submit to 3-4 hackathons in 6 months
[ ] Solana Frontier (Colosseum)
[ ] ETHGlobal events
[ ] Aleph ZK
[ ] Smaller community hackathons (Sigma, etc.)

GOAL FROM HACKATHONS:
- Win prize money ($5k-$50k typical)
- Land trong an accelerator (Colosseum gives $250k pre-seed)
- Get to demo trước investors / hiring managers
- Build connections via competition

PARALLEL: BRIDGE INCOME
Don't starve while doing this:
[ ] Take small contracting gigs (15-20h/week)
    Sources: Talent.io, Toptal, direct DMs
[ ] Smaller protocols, lower pay than full-time but flexible
[ ] Target $2-3k/month bridge income

LIFESTYLE:
[ ] Reduce expenses to fit reduced income
[ ] Treat self as "founder mode" not employee
[ ] Network với accelerators, VCs (warm intros only)
[ ] Build trong public very visibly (Twitter)
```

**Plan C execution checklist:**

```
[ ] Register for next Solana / ETHGlobal hackathon
[ ] Pick high-impact hackathon idea:
    - DeFi novel mechanism
    - AI agent infrastructure
    - Cross-chain UX innovation
    - Security tool
[ ] Build hackathon project full-time (4-6 weeks intensive)
[ ] Submit, even if not perfect (deadlines force shipping)
[ ] After hackathon (regardless of result):
    [ ] Cold-email hackathon judges (they often hire)
    [ ] Update Notion Hackathon DB
    [ ] Public demo video on Twitter
[ ] Repeat for 2nd, 3rd hackathon
[ ] After 3 hackathons: assess
    [ ] Won money → maybe extend
    [ ] Got into accelerator → take it
    [ ] Made connections → use them
    [ ] Nothing → return to job hunt with better story
```

---

### 10.3 SUSTAINABLE BURNOUT PROTOCOL

If at any point during Phase 1-4 you experience:

- 3+ days unable to focus
- 1+ week of no commits even with effort
- Negative thoughts về the journey > positive
- Physical symptoms (insomnia, gut issues, headaches)
- Mood < 4/10 for 2+ weeks

Then RUN this protocol:

```
IMMEDIATE (today):
[ ] Stop all coding for minimum 3 days
[ ] No Twitter, no Discord scrolling
[ ] Sleep at least 8 hours
[ ] Light exercise daily (walk, stretch)
[ ] Healthy meals
[ ] Talk to someone (partner, friend, family)

WITHIN 1 WEEK:
[ ] Honest assessment trong RETRO_BURNOUT.md:
    [ ] Why am I burning out specifically?
    [ ] Is the timeline realistic for my life?
    [ ] Is this the right plan for me?
[ ] Discuss với 1 mentor or trusted friend
[ ] If serious: see a therapist (mental health professional)

WHEN RETURNING (1-2 weeks later):
[ ] Reduce target hours by 25-30% temporarily
[ ] Cut current week's plan to absolute essentials
[ ] No Twitter pressure (don't post about returning)
[ ] Re-establish small wins: 1 small commit, 1 small task done
[ ] Build momentum slowly back

LONG TERM:
[ ] Build buffer week mỗi tháng (already in plan, observe rigorously)
[ ] 1 day off mỗi tuần (RULE-02, observe rigorously)
[ ] Quarterly: full week vacation if possible
[ ] Health > plan completion
```

The plan is rigid. The mission is bigger than the plan.

---

### 10.4 LIFE EVENT PROTOCOL

Real life happens. If you experience:

- Family medical emergency
- Personal medical issue
- Major relocation
- Significant relationship change
- Job loss (current employment)
- Financial crisis

Then:

```
PERMISSION TO PAUSE:
[ ] Stop the plan completely if needed
[ ] Don't feel guilty
[ ] Update Notion Phase Milestones với pause status

WHEN STABLE:
[ ] Reassess: do I still want this goal?
[ ] If YES: rebuild from current Phase, slower pace
[ ] If NO: that's also OK. Plan was a tool, not a contract.

DON'T:
[ ] Don't self-flagellate
[ ] Don't compare to others online
[ ] Don't push through medical issues
```

---

## ━━━ SECTION 11: HOW AGENT USES THIS FILE ━━━

This file is reference material, not daily-execution.

### Agent triggers

```
TRIGGER: End of week (Sunday evening)
  → Read Section 7.5 trigger checks
  → Run weekly Market Pulse (Section 9)
  → Update Notion

TRIGGER: End of month (last Sunday)
  → Run Section 7 monthly review fully
  → Generate RETRO_M[N].md

TRIGGER: End of phase (last day of phase)
  → Run Section 8 corresponding gate
  → Update Notion Decision Gates DB

TRIGGER: Section 9.3 conditions hit for 4+ weeks
  → Surface to user: "Plan B trigger met. Recommend pivot. Approve?"
  → On approval: run Section 10.1 checklist

TRIGGER: User reports burnout symptoms
  → Surface Section 10.3
  → Don't bypass — actually pause

TRIGGER: User reports life event
  → Surface Section 10.4
  → No judgement, support pause
```

### Agent communication style

When running protocols, agent should:

- Be honest, not aspirational
- Surface bad news fairly
- Avoid fake encouragement ("you got this!" hollow)
- Provide options, not commands
- Trust the user's judgement on life decisions
- Defer to user on values (career vs health, etc.)

---

## ━━━ APPENDIX: USEFUL RESOURCES BY PROTOCOL ━━━

**Monthly Review:**
- Andrej Karpathy retrospective patterns
- The Pragmatic Engineer monthly check-in template

**Decision Gates:**
- Levels.fyi for compensation benchmark
- LinkedIn job listing data

**Market Pulse:**
- web3.career
- electriccapital.com developer report
- Solana Foundation quarterly reports
- Pragmatic Engineer trends posts

**Plan B/C:**
- Talent.io (contracting)
- Colosseum (Solana hackathons)
- ETHGlobal (Ethereum hackathons)
- Toptal (high-end contracting)

**Burnout protocol:**
- Tim Ferriss "The 4-Hour Workweek" rest principles
- Cal Newport "Deep Work" pacing

---

*Protocols file v1.0 | Companion to make-plan*.md | Sync to Notion as reference page*
