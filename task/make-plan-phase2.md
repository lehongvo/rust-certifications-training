<!-- ============================================================
     AGENT EXECUTION PLAN — PHASE 2: BUILD
     Week 13–24 | 2026-08-01 → 2026-10-31
     Companion to make-plan.md (master + Phase 1)
     ============================================================ -->

# PHASE 2 — BUILD (W13–W24 | Aug 1 – Oct 31, 2026)

**Phase goal:** 2-3 mainnet protocols, real users, security-hardened code, network mở rộng.
**Success criteria for Q2 Gate (W24, Oct 22):**
- ≥ 2 protocols deployed mainnet với verifiable build
- ≥ 1 OSS PR merged vào Anchor/Solana Cookbook
- ≥ 30 active GitHub commits/month
- ≥ 1 networking response (DM, intro, referral hint)
- Encode Club Solana Bootcamp completed
- Otter Security Audit course in progress

**Calendar overview:**
```
M4 (Aug 2026)  W13 W14 W15 W16  — AMM mainnet + Lending design
M5 (Sep 2026)  W17 W18 W19 W20  — Lending build + security hardening
M6 (Oct 2026)  W21 W22 W23 W24  — Yield aggregator + Q2 Gate
```

---

## SECTION 4: PHASE 2 DAILY PLAN

### ▶ MONTH 4 (M4): AMM Mainnet + Lending Design
**Calendar:** 2026-08-01 → 2026-08-31
**Weekly Hours Target:** 15–20h
**Theme:** Polish AMM to production, design lending protocol, OSS contributions

---

#### ◆ WEEK 13 (W13): 2026-08-03 → 2026-08-09
**Theme:** AMM mainnet deploy + frontend polish
**Weekly Goal:** AMM live on mainnet với verified build, frontend production-ready

**W13 — MONDAY 2026-08-03**

```
PHASE 2 KICKOFF (1h):
[ ] Mở rust-certification.md, đọc lại Section 7 (Strategic Investment)
[ ] Mở Notion Phase Milestones, set Phase 2 status = Active
[ ] Reflect: review Phase 1 retrospective, identify top 3 lessons to apply

LEARN (2h):
[ ] Read: Solana Mainnet Deploy Best Practices
    URL: https://solana.com/docs/programs/deploying
[ ] Topics: program upgrades, buffer accounts, multisig authority
[ ] NOTE in LEARNING_LOG: differences between devnet and mainnet deploy

COMMIT:
[ ] Commit: "docs: phase 2 kickoff, mainnet deploy notes"
[ ] Twitter: "Phase 2 starts today. Going from devnet experiments to mainnet products. 🚀 Building 2 production protocols this quarter. #buildinpublic"
```

**W13 — TUESDAY 2026-08-04**

```
SECURITY AUDIT (3h): AMM PRE-MAINNET REVIEW
[ ] Run final security checklist on amm_program:
    [ ] All checked_add/sub/mul where math happens
    [ ] No unwrap() in production paths (use Result + custom errors)
    [ ] All Account constraints verified
    [ ] PDA bump seeds canonicalized
    [ ] No reinitialization vulnerability
    [ ] Fee math: rounding direction is house-favorable
    [ ] LP token math: no precision loss attacks
[ ] Run: cargo audit (check dependency CVEs)
[ ] Run: anchor build --verifiable (must succeed)
[ ] Document findings in amm_program/SECURITY.md

COMMIT:
[ ] Commit: "security: AMM pre-mainnet audit checklist complete"
```

**W13 — WEDNESDAY 2026-08-05**

```
MAINNET DEPLOY (2h): AMM
[ ] Fund deploy wallet với 2 SOL (need ~1.5 SOL cho program deploy)
[ ] Build verifiable: anchor build --verifiable
[ ] Verify hash matches GitHub release
[ ] Deploy: anchor deploy --provider.cluster mainnet
[ ] Set upgrade authority to multisig (or document plan to do so)
[ ] Record Mainnet Program ID in:
    - amm_program/README.md
    - karpathy-rust main README
    - Notion Projects DB

POST-DEPLOY (1h):
[ ] Verify on Solscan, copy verifiable badge
[ ] Initial pool: create test pool with 2 SPL tokens (small liquidity, ~$10)
[ ] Test swap on mainnet với phantom wallet
[ ] Take screenshot for portfolio

COMMIT:
[ ] Commit: "deploy: AMM live on mainnet [PROGRAM_ID]"
[ ] Twitter: "AMM is LIVE on Solana mainnet 🎉 Program ID: [ID]
    Verifiable build ✅
    Initial pool seeded ✅
    Frontend at: [URL]
    Try a swap and let me know what breaks. 🦀 #Solana"
```

**W13 — THURSDAY 2026-08-06**

```
FRONTEND POLISH (3h): AMM dApp PRODUCTION
[ ] Update mainnet program ID trong frontend env vars
[ ] Add network selector: devnet | mainnet (default mainnet)
[ ] Add transaction history view per user
[ ] Add total volume tracker (mock for now, real later)
[ ] Add "deployed contract" badge with Solscan link
[ ] Ensure error messages are user-friendly (no raw RPC errors)

COMMIT:
[ ] Commit: "feat: AMM frontend mainnet ready với network selector"
[ ] Deploy to Vercel: vercel --prod
[ ] Test live URL works correctly
```

**W13 — FRIDAY 2026-08-07**

```
INDEXING (3h): AMM ON-CHAIN DATA
[ ] Setup Helius webhook for AMM program events
    URL: https://docs.helius.dev/webhooks-and-websockets/what-are-webhooks
[ ] Listen for: SwapExecuted, LiquidityAdded, LiquidityRemoved events
[ ] Store events in Postgres or simple JSON file (start small)
[ ] Build /api/stats endpoint: returns 24h volume, total swaps, unique users

COMMIT:
[ ] Commit: "feat: AMM indexer + stats API via Helius webhooks"
```

**W13 — SATURDAY 2026-08-08**

```
DEEP WORK (4h): LENDING PROTOCOL DESIGN
[ ] Read: Compound V2 protocol docs (you know this from EVM)
    URL: https://docs.compound.finance/v2/
[ ] Read: Solend docs (Solana lending)
    URL: https://docs.solend.fi/
[ ] Read: Kamino Lend architecture
    URL: https://docs.kamino.finance/

DESIGN DOCUMENT (2h):
[ ] Create: projects/lending_protocol/DESIGN.md
    Sections:
    [ ] Account model:
        - Market (per asset): { mint, vault, total_borrowed, total_supplied, interest_rate_model, ... }
        - UserPosition (PDA from [user, market]): { collateral_amount, borrow_amount, last_update_slot }
        - LendingPool (top-level): { admin, markets[], oracle_program }
    [ ] Instructions: 
        - init_market, deposit, withdraw, borrow, repay, liquidate
    [ ] Interest rate model (start simple): 
        - Linear: rate = base + utilization * slope
        - Update interest accrual on every interaction
    [ ] Liquidation:
        - Health factor = collateral_value * collateral_factor / borrow_value
        - Liquidate if health < 1.0
        - Liquidator gets liquidation_bonus discount

COMMIT:
[ ] Commit: "docs: lending_protocol design document v1"

BLOG (1h):
[ ] Draft: "Designing a Lending Protocol on Solana — From Compound to Anchor"
    Outline: account model differences, interest accrual challenges, liquidation flow
```

**W13 — SUNDAY 2026-08-09**

```
REVIEW (30 min):
[ ] W13 KPI: AMM mainnet ✅, frontend updated, indexer setup, lending designed
[ ] Update Notion Daily Plan: mark W13 entries Done
[ ] Publish AMM mainnet announcement on LinkedIn

REST:
[ ] No code, no docs, no Twitter past 6PM
```

**W13 DELIVERABLES:**
```
[ ] AMM deployed mainnet với verifiable build (Program ID recorded)
[ ] AMM frontend production-ready, deployed Vercel
[ ] Helius webhook indexer for AMM events
[ ] Lending protocol design document v1
[ ] 1 Twitter post + 1 LinkedIn post (mainnet announcement)
[ ] Commit streak: 6/6 weekdays + Saturday
```

---

#### ◆ WEEK 14 (W14): 2026-08-10 → 2026-08-16
**Theme:** Lending protocol scaffold + interest rate math
**Weekly Goal:** Lending protocol có deposit/withdraw working trên devnet

**W14 — MONDAY 2026-08-10**

```
BUILD (3h): LENDING PROTOCOL SCAFFOLD
[ ] anchor init lending_protocol
[ ] Define Account structs trong programs/lending_protocol/src/state.rs:
    [ ] LendingPool { admin: Pubkey, num_markets: u8, paused: bool }
    [ ] Market { mint, vault, total_supplied, total_borrowed, supply_rate, borrow_rate, last_update_slot }
    [ ] UserPosition { user, market, collateral, borrowed, last_interest_update }
[ ] Define instruction handlers (empty bodies):
    init_pool, init_market, deposit, withdraw, borrow, repay, liquidate
[ ] anchor build (must succeed)

COMMIT:
[ ] Commit: "feat: lending_protocol scaffold + account definitions"
```

**W14 — TUESDAY 2026-08-11**

```
BUILD (3h): DEPOSIT + WITHDRAW
[ ] Implement init_pool và init_market (admin only)
[ ] Implement deposit:
    [ ] Transfer SPL tokens from user → market vault (CPI)
    [ ] Update Market.total_supplied
    [ ] Create or update UserPosition
    [ ] Mint receipt tokens (sToken pattern, like Compound's cToken)
    [ ] Calculate exchange rate based on accrued interest
[ ] Implement withdraw:
    [ ] Burn receipt tokens
    [ ] Calculate underlying amount
    [ ] Transfer from vault → user
    [ ] Verify user has no outstanding borrows preventing withdraw

TEST:
[ ] anchor test (deposit + withdraw scenarios)
[ ] Deploy devnet

COMMIT:
[ ] Commit: "feat: lending deposit/withdraw with sToken receipt pattern"
```

**W14 — WEDNESDAY 2026-08-12**

```
LEARN (2h): INTEREST RATE MODELS
[ ] Read: Compound's JumpRateModel
    GitHub: compound-finance/compound-protocol/contracts/JumpRateModel.sol
[ ] Read: Aave's interest rate strategy
[ ] Note: simple linear model for v1, can upgrade later

BUILD (1h): INTEREST ACCRUAL
[ ] Implement update_interest (internal):
    [ ] Calculate elapsed slots since last update
    [ ] interest = borrow_rate * total_borrowed * elapsed / SLOTS_PER_YEAR
    [ ] Update total_borrowed += interest
    [ ] Update supply_rate based on utilization: supply_rate = borrow_rate * utilization
    [ ] Set last_update_slot = current_slot
[ ] Call update_interest at start of every state-changing instruction

COMMIT:
[ ] Commit: "feat: lending interest accrual + linear rate model"
```

**W14 — THURSDAY 2026-08-13**

```
BUILD (3h): BORROW + REPAY
[ ] Implement borrow(amount):
    [ ] Verify user collateral covers loan với LTV check
    [ ] LTV = collateral_value * 0.75 (simple, hardcode for now)
    [ ] Update UserPosition.borrowed
    [ ] Update Market.total_borrowed
    [ ] Transfer from vault → user (CPI invoke_signed)
    [ ] Emit Borrowed event
[ ] Implement repay(amount):
    [ ] Calculate accrued interest, add to debt
    [ ] Transfer from user → vault (CPI)
    [ ] Reduce UserPosition.borrowed (allow over-repay = withdraw extra)

TEST:
[ ] anchor test scenarios:
    [ ] deposit collateral
    [ ] borrow within limit
    [ ] borrow over limit → expect error
    [ ] repay full debt
    [ ] withdraw collateral after repay

COMMIT:
[ ] Commit: "feat: lending borrow/repay với LTV check + interest"
```

**W14 — FRIDAY 2026-08-14**

```
ORACLE INTEGRATION (3h):
[ ] Read: Pyth Network for Solana price feeds
    URL: https://docs.pyth.network/price-feeds/use-real-time-data/solana
[ ] Read: Switchboard alternative
    URL: https://docs.switchboard.xyz/

BUILD:
[ ] Add price oracle integration to lending_protocol:
    [ ] Use Pyth price account in deposit/borrow/withdraw
    [ ] Calculate USD value: amount * price.price * 10^price.expo
    [ ] LTV check now uses real price ratios
[ ] Test với mainnet Pyth feed (read-only on devnet)

COMMIT:
[ ] Commit: "feat: lending Pyth oracle integration for USD pricing"
```

**W14 — SATURDAY 2026-08-15**

```
DEEP WORK (4h): LIQUIDATION
[ ] Implement liquidate instruction:
    [ ] Anyone can call (permissionless)
    [ ] Check user's health factor:
        health = sum(collateral_value * collateral_factor) / sum(borrow_value)
    [ ] Require health < 1.0 (under-collateralized)
    [ ] Liquidator pays portion of borrower's debt
    [ ] Liquidator receives equivalent collateral + bonus (5-10%)
    [ ] Update UserPosition để reflect new state
    [ ] Cap liquidation: max 50% of position per call (close factor)

TEST:
[ ] Test scenario: 
    1. User deposits 100 SOL @ $150 → $15,000 collateral
    2. User borrows 10,000 USDC (within LTV)
    3. SOL drops to $100 (mock oracle update)
    4. Health factor = 10,000 / 15,000 → wait, recalc...
       health = (100 * 100 * 0.75) / 10,000 = 7,500 / 10,000 = 0.75 (under-collateralized)
    5. Liquidator calls liquidate, repays 5,000 USDC
    6. Liquidator receives equivalent SOL + 5% bonus

COMMIT:
[ ] Commit: "feat: lending liquidation với close factor + bonus"
```

**W14 — SUNDAY 2026-08-16**

```
REVIEW (30 min):
[ ] W14 KPI fill in Notion
[ ] Plan W15: testing focus, security pass

REST:
```

**W14 DELIVERABLES:**
```
[ ] lending_protocol scaffolded with all instructions implemented
[ ] Deposit/withdraw working
[ ] Borrow/repay với LTV check
[ ] Interest accrual với linear rate model
[ ] Pyth oracle integration
[ ] Liquidation logic
[ ] 8+ unit tests passing
[ ] Devnet deploy
[ ] Commit streak: 6/6
```

---

#### ◆ WEEK 15 (W15): 2026-08-17 → 2026-08-23
**Theme:** Lending tests + security + frontend integration
**Weekly Goal:** Lending protocol ready for mainnet review

**W15 — MONDAY 2026-08-17**

```
TEST EXPANSION (3h):
[ ] Add edge case tests cho lending_protocol:
    [ ] Multi-market: deposit market A, borrow market B
    [ ] Self-liquidation should fail
    [ ] Liquidate exactly at health = 1.0 (boundary)
    [ ] Repay more than borrowed (should refund excess)
    [ ] Withdraw exactly LTV limit
    [ ] Concurrent borrows from same position
    [ ] Interest accumulates correctly over multiple interactions
[ ] Mock time progression: use Clock sysvar mocking

COMMIT:
[ ] Commit: "test: lending_protocol edge cases (10+ scenarios)"
```

**W15 — TUESDAY 2026-08-18**

```
SECURITY AUDIT (3h): LENDING PROTOCOL
[ ] Apply Sealevel 9 attacks checklist
[ ] Specific lending attack vectors:
    [ ] Oracle manipulation (price spike during liquidation)
    [ ] Re-entrancy via CPI (refresh accounts after CPI calls)
    [ ] Rounding errors that favor user vs protocol
    [ ] Donation attack (sending tokens directly to vault, breaking exchange rate)
    [ ] Flash loan attack (deposit, borrow, withdraw in 1 tx)
    [ ] Bad debt accumulation if liquidation fails
[ ] Document findings in SECURITY.md
[ ] Fix issues found

COMMIT:
[ ] Commit: "security: lending audit pass — fixes for donation attack + rounding"
```

**W15 — WEDNESDAY 2026-08-19**

```
LEARN (2h): SOLANA TRANSACTION COMPOSING
[ ] Read: Solana Cookbook — Combining Instructions
    URL: https://solanacookbook.com/references/basic-transactions.html
[ ] Topics: priority fees, compute budget, lookup tables (ALTs)

PRACTICE (1h):
[ ] Add compute budget instructions to lending tests
[ ] Test priority fee impact during congestion

COMMIT:
[ ] Commit: "feat: lending tests use compute budget + priority fees"
```

**W15 — THURSDAY 2026-08-20**

```
FRONTEND BUILD (3h): LENDING dApp
[ ] Use existing AMM frontend as base, fork to lending-frontend
[ ] OR: combine into single dapp với routing
[ ] Pages:
    [ ] / — Markets overview (per asset stats)
    [ ] /supply — Deposit collateral
    [ ] /borrow — Borrow against collateral
    [ ] /position — User position dashboard (health factor, balances)
    [ ] /liquidate — Liquidation interface (for liquidators)
[ ] Real-time health factor calculation
[ ] APY display (supply + borrow rates)

COMMIT:
[ ] Commit: "feat: lending frontend với markets + position pages"
```

**W15 — FRIDAY 2026-08-21**

```
FRONTEND POLISH (2h):
[ ] Add: Health factor visualization (color: green > 1.5, yellow 1.1-1.5, red < 1.1)
[ ] Add: Liquidation history (recent liquidations with PnL for liquidator)
[ ] Add: Network selector (devnet/mainnet)
[ ] Mobile responsive check
[ ] Test full user flow on devnet

LEARN (1h):
[ ] Read: Apply Otter Security Audit Course materials (chapter 1-2)
    Otter started — make sure to actively follow

COMMIT:
[ ] Commit: "polish: lending frontend UX + health visualization"
```

**W15 — SATURDAY 2026-08-22**

```
DEEP WORK (4h): COMPREHENSIVE INTEGRATION TESTS
[ ] Write integration test suite covering:
    [ ] User journey 1: Supplier earns interest
        - Deposit 1000 USDC → wait 30 days (mock) → withdraw with interest
    [ ] User journey 2: Borrower with collateral
        - Deposit 10 SOL → borrow 500 USDC → repay → withdraw
    [ ] User journey 3: Liquidation flow
        - Same as above but oracle drops, liquidator profits
    [ ] User journey 4: Multi-market
        - Use SOL as collateral for USDC borrow, SOL for ETH borrow
    [ ] Stress test: 100 users, random ops, verify invariants hold
[ ] Run on local validator with --reset

COMMIT:
[ ] Commit: "test: lending integration test suite — 4 journeys + stress test"

BLOG (1h):
[ ] Draft: "Building a Lending Protocol on Solana: Architecture Decisions"
    Sections: account model, oracle integration, liquidation logic, gotchas
```

**W15 — SUNDAY 2026-08-23**

```
[ ] W15 KPI fill
[ ] Publish lending blog post
[ ] REST
```

**W15 DELIVERABLES:**
```
[ ] Lending protocol fully tested (15+ tests passing)
[ ] Security audit pass với fixes
[ ] Lending frontend with health visualization
[ ] Integration test suite (4 user journeys)
[ ] 1 blog post published
[ ] Otter Security Course chapter 1-2 done
```

---

#### ◆ WEEK 16 (W16): 2026-08-24 → 2026-08-30
**Theme:** Lending mainnet + Encode Club final + buffer week prep
**Weekly Goal:** Lending mainnet, Encode Club cert obtained

**W16 — MONDAY 2026-08-24**

```
PRE-MAINNET CHECKLIST (3h):
[ ] Final security pass on lending_protocol
[ ] Verify: anchor build --verifiable produces deterministic hash
[ ] Tag GitHub release: v1.0-mainnet
[ ] Update README với deploy instructions, Program ID placeholder
[ ] Prepare announcement post (don't publish yet)

DEPLOY (1h):
[ ] Fund deploy wallet (~2 SOL needed)
[ ] anchor deploy --provider.cluster mainnet
[ ] Record Mainnet Program ID
[ ] Verify on Solscan

COMMIT:
[ ] Commit: "deploy: lending_protocol live on mainnet [PROGRAM_ID]"
```

**W16 — TUESDAY 2026-08-25**

```
POST-DEPLOY (2h):
[ ] Update lending frontend với mainnet program ID
[ ] Deploy frontend production
[ ] Initial market setup: USDC market, SOL market (small caps for safety)
[ ] Add to AMM frontend: link to lending dapp (cross-promo)

ANNOUNCEMENT (1h):
[ ] Twitter thread (5 tweets):
    1. "Just deployed my second mainnet protocol on Solana 🎉"
    2. "Lending protocol with [features list]"
    3. "Code: [GitHub] | Frontend: [URL] | Program ID: [ID]"
    4. "What I learned building this..."
    5. "Try it (small amounts only) and feedback welcome"
[ ] Dev.to post: "Lending Protocol Live on Solana Mainnet — Stats & Lessons"
[ ] LinkedIn post

COMMIT:
[ ] Commit: "deploy: lending frontend mainnet + initial markets"
```

**W16 — WEDNESDAY 2026-08-26**

```
ENCODE CLUB FINAL (3h):
[ ] Complete remaining Encode Club Bootcamp modules
[ ] Submit final project (Anchor program with tests)
[ ] If grade pending: contact bootcamp coordinator
[ ] Save certificate to repo (assets/encode-club-cert.png)
[ ] Update LinkedIn Education với Encode Club cert

COMMIT:
[ ] Commit: "docs: Encode Club Solana Bootcamp completed + cert"
```

**W16 — THURSDAY 2026-08-27**

```
OSS CONTRIBUTION #3 (3h):
[ ] Browse Solana ecosystem repos for "good first issue":
    - solana-developers/solana-cookbook
    - coral-xyz/anchor
    - solana-labs/solana
    - metaplex-foundation/mpl-token-metadata
[ ] Pick a meaningful issue (not trivial typo)
[ ] Implement fix với tests
[ ] Submit PR
[ ] Track in Notion Projects DB → OSS Contributions

COMMIT:
[ ] Commit in fork + PR submitted
```

**W16 — FRIDAY 2026-08-28**

```
NETWORKING (2h):
[ ] Engage in 5 Solana Discord conversations (don't spam)
[ ] Comment on 3 Twitter threads from hiring managers (substantive)
[ ] DM 2 engineers from target companies (intro yourself, share project)
    Template:
    "Hi [name], saw your work on [specific thing]. I'm a Solidity dev
    transitioning to Solana, just shipped [project link]. Would love
    your 5-min feedback when convenient. Thanks!"

LEARN (1h):
[ ] Otter Security Course chapter 3 (Solana Audit Methodology)

COMMIT:
[ ] Update networking log
[ ] Commit: "docs: networking log W16"
```

**W16 — SATURDAY 2026-08-29**

```
DEEP WORK (3h): YIELD AGGREGATOR DESIGN
[ ] Read: Yearn V2 strategies (EVM)
[ ] Read: Kamino strategies (Solana)
[ ] Design simple yield aggregator on Solana:
    [ ] Vault accepts deposits of SPL token X
    [ ] Strategy contract decides allocation: how much in lending vs AMM LP
    [ ] Periodic rebalance keeps target weights
    [ ] Performance fee on profits
[ ] Document trong projects/yield_aggregator/DESIGN.md

BLOG (1h):
[ ] Draft: "From Yearn to Solana — Designing a Yield Aggregator"
```

**W16 — SUNDAY 2026-08-30**

```
[ ] W16 KPI fill
[ ] M4 retrospective: what worked, what didn't
[ ] REST
```

**W16 DELIVERABLES:**
```
[ ] Lending protocol on MAINNET với verifiable build
[ ] Lending frontend production
[ ] Encode Club Bootcamp cert (or substitute)
[ ] OSS contribution #3 (PR submitted)
[ ] Yield aggregator design doc
[ ] 5 networking touchpoints
[ ] 2 blog posts in M4
```

**M4 (Aug) RETROSPECTIVE CHECKPOINT:**
```
[ ] 2 mainnet protocols (AMM + Lending) ✅
[ ] 3 OSS PRs total
[ ] Encode Club cert
[ ] Otter Security course in progress (target: complete by W20)
[ ] Network: 5+ touchpoints
[ ] Blog: 4+ posts in Phase 2 so far
[ ] Hours: 60-80h target
```

---

### ▶ MONTH 5 (M5): Lending Hardening + Yield Aggregator + Audit Course
**Calendar:** 2026-08-31 → 2026-09-30
**Weekly Hours Target:** 15–20h
**Theme:** Production hardening, audit skills, yield aggregator implementation

---

#### ◆ WEEK 17 (W17): 2026-08-31 → 2026-09-06
**Theme:** Yield aggregator scaffold + Otter Security deep dive

**W17 — MONDAY 2026-08-31**

```
BUILD (3h): YIELD AGGREGATOR SCAFFOLD
[ ] anchor init yield_aggregator
[ ] Define accounts:
    [ ] Vault { admin, accepted_mint, total_assets, total_shares, strategies[] }
    [ ] Strategy { type: enum, allocation_bps: u16, address: Pubkey }
    [ ] UserShares { user, vault, shares }
[ ] Define instructions:
    [ ] init_vault, set_strategy_weights, deposit, withdraw, harvest, rebalance
[ ] Implement deposit/withdraw with share-based accounting

COMMIT:
[ ] Commit: "feat: yield_aggregator scaffold + share-based vault"
```

**W17 — TUESDAY 2026-09-01**

```
BUILD (3h): STRATEGY: LENDING DEPOSIT
[ ] Implement Lending Strategy:
    [ ] CPI to lending_protocol.deposit
    [ ] Track sToken balance held by vault
    [ ] On harvest: redeem some sTokens to realize interest
[ ] Test với own lending_protocol on devnet

COMMIT:
[ ] Commit: "feat: yield aggregator lending strategy với CPI"
```

**W17 — WEDNESDAY 2026-09-02**

```
BUILD (3h): STRATEGY: AMM LP
[ ] Implement AMM LP Strategy:
    [ ] CPI to amm_program.add_liquidity (50/50 split)
    [ ] Track LP tokens held
    [ ] On harvest: realize trading fees by removing some liquidity, re-adding
[ ] Edge case: handle impermanent loss accounting

COMMIT:
[ ] Commit: "feat: yield aggregator AMM strategy với LP fee harvesting"
```

**W17 — THURSDAY 2026-09-03**

```
BUILD (2h): REBALANCE LOGIC
[ ] Implement rebalance instruction (anyone can call):
    [ ] Read current allocations from each strategy
    [ ] Calculate diff from target_weights
    [ ] If diff > 5%: trigger rebalance moves
    [ ] Limit rebalance to max 25% of TVL per call (safety)

LEARN (1h):
[ ] Otter Security Course chapter 4 (CPI security)
[ ] Apply learnings to yield_aggregator

COMMIT:
[ ] Commit: "feat: yield aggregator rebalance với safety limits"
```

**W17 — FRIDAY 2026-09-04**

```
TEST (3h):
[ ] Integration tests for yield aggregator:
    [ ] Deposit USDC → vault deploys to lending → user withdraws với interest
    [ ] Multi-strategy: 70% lending + 30% LP
    [ ] Rebalance after market move
    [ ] Harvest realizes profits
    [ ] Performance fee deducted correctly
[ ] anchor test all passing

COMMIT:
[ ] Commit: "test: yield aggregator 6 integration scenarios"
```

**W17 — SATURDAY 2026-09-05**

```
DEEP WORK (4h): SECURITY AUDIT — YIELD AGGREGATOR
[ ] Apply: Sealevel 9 attacks
[ ] Specific yield aggregator attacks:
    [ ] Inflation attack (first depositor exploit)
    [ ] Strategy collusion (malicious strategy drains vault)
    [ ] Donation attack on share price
    [ ] Front-running rebalance for arbitrage
    [ ] Rounding errors in share calculation
[ ] Mitigations:
    [ ] Initial mint to dead address (0x000) to prevent inflation
    [ ] Whitelist strategies (admin-only addStrategy)
    [ ] Cap rebalance frequency và size
    [ ] Use ceiling rounding for fees, floor for user shares
[ ] Document trong SECURITY.md

COMMIT:
[ ] Commit: "security: yield aggregator audit + mitigations"
```

**W17 — SUNDAY 2026-09-06**

```
[ ] W17 KPI
[ ] REST
```

**W17 DELIVERABLES:**
```
[ ] Yield aggregator scaffolded với 2 strategies (lending + LP)
[ ] Rebalance logic working
[ ] Security audit pass
[ ] 6 integration tests passing
[ ] Otter Security chapter 4 done
[ ] Devnet deploy
```

---

#### ◆ WEEK 18 (W18): 2026-09-07 → 2026-09-13
**Theme:** Yield aggregator polish + frontend + Otter halfway

**W18 — MONDAY 2026-09-07**

```
BUILD (3h): FRONTEND FOR YIELD AGGREGATOR
[ ] Add yield page to existing dapp
[ ] UI components:
    [ ] Vault overview (TVL, current APY, strategy breakdown chart)
    [ ] Deposit form
    [ ] Withdraw form
    [ ] User position (shares, value, performance vs deposit)
    [ ] Strategy table (allocation, performance, last harvest)
[ ] Real-time APY calculation từ on-chain data

COMMIT:
[ ] Commit: "feat: yield vault frontend với strategy breakdown"
```

**W18 — TUESDAY 2026-09-08**

```
LEARN (3h): OTTER SECURITY DEEP DIVE
[ ] Chapter 5: Token Program Vulnerabilities
    [ ] Authority confusion attacks
    [ ] Mint authority misuse
    [ ] Delegate exploitation
[ ] Apply learnings to your token_manager program (revisit)
[ ] Found vulnerabilities? Fix immediately

COMMIT:
[ ] Commit: "security: token_manager fixes from Otter chapter 5 review"
```

**W18 — WEDNESDAY 2026-09-09**

```
LEARN (2h): OTTER CHAPTER 6
[ ] Chapter 6: PDA Security Patterns
    [ ] Bump seed manipulation
    [ ] Seed collision attacks
    [ ] Authority impersonation via PDA

REVIEW (1h):
[ ] Audit all your programs cho PDA issues:
    [ ] counter_program ✓
    [ ] voting_program ✓
    [ ] token_manager — check
    [ ] staking_program — check
    [ ] amm_program — check
    [ ] lending_protocol — check
    [ ] yield_aggregator — check

COMMIT:
[ ] Commit: "security: PDA pattern review + fixes across programs"
```

**W18 — THURSDAY 2026-09-10**

```
BUILD (3h): YIELD AGGREGATOR — ADD ANOTHER STRATEGY
[ ] Implement: Marinade Finance staking strategy
    [ ] CPI to Marinade's deposit_sol → receive mSOL
    [ ] Track mSOL held by vault
    [ ] On harvest: rate of mSOL/SOL increases over time = our profit
[ ] Now vault can support: cash, lending, AMM LP, staked SOL allocations

COMMIT:
[ ] Commit: "feat: yield aggregator + Marinade staking strategy"
```

**W18 — FRIDAY 2026-09-11**

```
INDEXING + ANALYTICS (3h):
[ ] Setup Helius webhooks for lending + yield programs
[ ] Build /api/portfolio endpoint (returns user's total positions across all 3 programs)
[ ] Add portfolio dashboard page to frontend

COMMIT:
[ ] Commit: "feat: cross-program portfolio dashboard với indexer"
```

**W18 — SATURDAY 2026-09-12**

```
DEEP WORK (4h): MAINNET YIELD AGGREGATOR DEPLOY
[ ] Final security review
[ ] Verifiable build
[ ] Deploy mainnet
[ ] Initial vault: USDC vault với conservative allocations
    - 60% lending (your protocol)
    - 30% AMM LP (your AMM with stablecoin pair)
    - 10% cash reserve
[ ] Self-deposit $50 USDC to demonstrate working
[ ] Record program ID, update all docs

COMMIT:
[ ] Commit: "deploy: yield_aggregator MAINNET + first vault initialized"

ANNOUNCEMENT:
[ ] Twitter: "3 mainnet protocols now! 🎉
    AMM + Lending + Yield Aggregator
    All composable: yield vault uses my own AMM and Lending
    Live: [URL]
    Code: [GitHub]
    #Solana #DeFi"
```

**W18 — SUNDAY 2026-09-13**

```
[ ] W18 KPI
[ ] LinkedIn announcement (3rd mainnet)
[ ] REST
```

**W18 DELIVERABLES:**
```
[ ] Yield aggregator MAINNET với verifiable build (3rd protocol total)
[ ] 3 strategies: Lending, AMM LP, Marinade Staking
[ ] Cross-program portfolio dashboard
[ ] Otter Security chapters 5-6 done
[ ] Composability proven: vault uses my own AMM + Lending
[ ] Twitter + LinkedIn announcement
```

---

#### ◆ WEEK 19 (W19): 2026-09-14 → 2026-09-20
**Theme:** Buffer week — review, refactor, content
**Note:** This is the buffer week per RULE-03. NO new features.

**W19 — MONDAY 2026-09-14**

```
BUFFER MODE (RULE-03): No new features this week.
Focus: refactor, test coverage, documentation, content

REFACTOR (3h):
[ ] Review all 3 mainnet programs for code quality
[ ] Apply DRY principle: extract common patterns into shared module
[ ] Naming consistency: rename unclear variables
[ ] Run cargo clippy --fix với manual review

COMMIT:
[ ] Commit: "refactor: code quality pass on AMM + Lending + Yield"
```

**W19 — TUESDAY 2026-09-15**

```
TEST COVERAGE (3h):
[ ] Run: cargo tarpaulin --out Html (coverage report)
[ ] Identify untested branches
[ ] Add tests to bring coverage to 80%+ on each program
[ ] Run: anchor test (full suite, must pass)

COMMIT:
[ ] Commit: "test: coverage to 80%+ on all 3 mainnet programs"
```

**W19 — WEDNESDAY 2026-09-16**

```
DOCUMENTATION (3h):
[ ] Update each program's README to production quality:
    [ ] Architecture diagram (ASCII or draw.io image)
    [ ] All instructions documented (parameters, errors, events)
    [ ] Deploy instructions for fresh setup
    [ ] Security considerations section
    [ ] Known limitations
    [ ] Roadmap for v2
[ ] Update karpathy-rust main README:
    [ ] Add full project index table
    [ ] Add stats: programs deployed, tests, OSS PRs, blog posts

COMMIT:
[ ] Commit: "docs: production-quality READMEs across all programs"
```

**W19 — THURSDAY 2026-09-17**

```
CONTENT BLITZ (3h):
[ ] Write Dev.to: "I Built 3 Composable DeFi Protocols on Solana — Here's How They Talk to Each Other"
    Focus on CPI architecture, security considerations, lessons
[ ] Twitter thread (8 tweets) summarizing 4 months of work
[ ] LinkedIn long-form post
[ ] Schedule posts via Buffer or similar

COMMIT:
[ ] Commit: "content: 3-protocol composability article + threads"
```

**W19 — FRIDAY 2026-09-18**

```
NETWORKING (2h):
[ ] Reach out to 5 senior engineers từ target companies
[ ] Approach: share what you've built, ask 1 specific technical question
[ ] Examples of good DM: "Saw your tweet about MEV on Solana. I'm building [X] and curious how you'd think about [specific Y]."
[ ] Don't pitch yourself, ask substantive question

LEARN (1h):
[ ] Otter Security chapter 7

COMMIT:
[ ] Commit: "docs: networking log W19 + Otter ch7 notes"
```

**W19 — SATURDAY 2026-09-19**

```
PORTFOLIO PREP (4h):
[ ] Create projects/portfolio_dapp:
    [ ] Single page frontend showcasing all 3 protocols
    [ ] Hero section: name, role, 1-line bio
    [ ] Projects grid: each program card với stats
    [ ] About: skills, experience timeline
    [ ] Contact: GitHub, Twitter, LinkedIn, email
[ ] Use Next.js + Tailwind, clean modern design
[ ] Deploy to portfolio.lehongvo.dev (or similar)

COMMIT:
[ ] Commit: "feat: portfolio dapp at portfolio.lehongvo.dev"
```

**W19 — SUNDAY 2026-09-20**

```
[ ] W19 KPI fill
[ ] Publish blog post (composability article)
[ ] REST — buffer week reflection: am I burning out?
```

**W19 DELIVERABLES:**
```
[ ] All programs refactored to production quality
[ ] Test coverage 80%+ across mainnet programs
[ ] Production-quality READMEs
[ ] Composability blog post published
[ ] Portfolio dapp live at portfolio.lehongvo.dev
[ ] 5 senior engineer DMs sent
[ ] Otter Security chapter 7 done
```

---

#### ◆ WEEK 20 (W20): 2026-09-21 → 2026-09-27
**Theme:** Otter Security cert + Audit practice + Pre-Phase 3 prep

**W20 — MONDAY 2026-09-21**

```
LEARN (3h): OTTER SECURITY FINAL CHAPTERS
[ ] Chapter 8: Real-World Audit Case Studies
[ ] Chapter 9: Audit Reports Writing
[ ] Read 3 published audit reports (find on Otter or company blogs)

COMMIT:
[ ] Commit: "docs: Otter Security chapters 8-9 + audit report studies"
```

**W20 — TUESDAY 2026-09-22**

```
PRACTICE AUDIT (3h):
[ ] Pick a public Solana program with known vulnerabilities (educational)
    Example: ethonsolana wormhole exploit, or any post-mortem report
[ ] Audit it yourself, write findings report
[ ] Compare your findings vs the actual exploit
[ ] Note gaps trong your auditing skill

COMMIT:
[ ] Commit: "practice: self-audit of [program] với findings comparison"
```

**W20 — WEDNESDAY 2026-09-23**

```
AUDIT (3h): SELF-AUDIT WRITE-UP
[ ] Write formal audit report cho your own lending_protocol
[ ] Format: industry standard (severity, vulnerability, recommendation, references)
[ ] Sections:
    [ ] Executive summary
    [ ] Scope
    [ ] Findings (Critical/High/Medium/Low/Info)
    [ ] Recommendations
    [ ] Appendix: methodology
[ ] Save as lending_protocol/AUDIT_REPORT_v1.md

COMMIT:
[ ] Commit: "docs: lending_protocol formal self-audit report"
```

**W20 — THURSDAY 2026-09-24**

```
COMPLETE OTTER CERT (2h):
[ ] Complete Otter Security final assessment
[ ] Submit final report
[ ] Save certificate
[ ] Update LinkedIn skills + Education

NETWORKING (1h):
[ ] Engage 3 audit-focused devs trên Twitter
[ ] Comment substantively on audit findings posts

COMMIT:
[ ] Commit: "achievement: Otter Security Audit Course completed"
```

**W20 — FRIDAY 2026-09-25**

```
PHASE 3 RESEARCH (3h):
[ ] Research target companies cho Phase 3 apply (build list of 30):
    Categories:
    Tier 1 (dream): Solana Labs, Anza, Jito Labs, Helius
    Tier 2 (strong fit): Drift, Kamino, Marinade, Meteora
    Tier 3 (warm-up): smaller protocols, freelance gigs
[ ] For each: open roles, hiring manager Twitter, recent news
[ ] Add to Notion Job Application Tracker DB

COMMIT:
[ ] Commit: "docs: Phase 3 target companies list (30) seeded in Notion"
```

**W20 — SATURDAY 2026-09-26**

```
DEEP WORK (4h): ZK INTRO PREP
[ ] Read: Zero Knowledge Proofs MOOC introduction
    URL: https://zk-learning.org/
[ ] Watch: Vitalik's "ZK-SNARKs in 30 minutes"
[ ] Read: RareSkills ZK Book chapter 1 (free)
[ ] NOTE in LEARNING_LOG: "What I think I understand about ZK proofs"
    Goal: not master, just orient before Phase 3 deep dive

BLOG (1h):
[ ] Draft: "I Just Started Learning ZK Proofs as a Solidity Dev — Here's My Mental Model"
    Pitch: from outsider perspective, what's the right way to understand it
```

**W20 — SUNDAY 2026-09-27**

```
[ ] W20 KPI
[ ] M5 retrospective: 5 months done, what's next
[ ] REST
```

**W20 DELIVERABLES:**
```
[ ] Otter Security Audit certificate
[ ] Self-audit report cho lending_protocol (formal format)
[ ] Practice audit case study completed
[ ] 30-company target list in Notion Job DB
[ ] ZK basics: 4-6h intro reading
[ ] Otter Security course 100% complete
```

**M5 (Sep) RETROSPECTIVE CHECKPOINT:**
```
[ ] 3 mainnet protocols ✅ (target was 2-3)
[ ] Otter Security cert ✅
[ ] OSS PRs: 3+ submitted
[ ] Network: 10+ touchpoints
[ ] Portfolio dapp live
[ ] Blog: 8+ posts in Phase 2
[ ] Hours: 60-80h target
```

---

### ▶ MONTH 6 (M6): Polish + Q2 Gate Prep
**Calendar:** 2026-09-28 → 2026-10-31
**Weekly Hours Target:** 15–20h
**Theme:** OSS deep contribution, ZK intro, networking acceleration, Q2 Gate

---

#### ◆ WEEK 21 (W21): 2026-09-28 → 2026-10-04
**Theme:** OSS meaningful contribution + ZK study

**W21 — MONDAY 2026-09-28**

```
OSS DEEP CONTRIBUTION (3h):
[ ] Find a substantive issue (not trivial) in major Solana repo:
    - Anchor: feature request, performance issue
    - Solana program library: missing functionality
[ ] Comment on issue thread expressing intent to work
[ ] Fork, branch, start implementation
[ ] Estimate: 5-10h work this week

COMMIT:
[ ] Commit in fork: initial implementation
```

**W21 — TUESDAY 2026-09-29**

```
OSS CONTINUE (3h):
[ ] Continue feature work
[ ] Write tests
[ ] Engage on issue thread với progress updates

COMMIT:
[ ] Commit in fork
```

**W21 — WEDNESDAY 2026-09-30**

```
OSS POLISH (3h):
[ ] Code review your own PR
[ ] Add documentation
[ ] Submit PR with detailed description
[ ] Tag relevant maintainers

COMMIT:
[ ] PR submitted, status: in review
```

**W21 — THURSDAY 2026-10-01**

```
LEARN ZK (2h):
[ ] RareSkills ZK Book chapters 2-4
[ ] Topics: arithmetic circuits, polynomial commitments
[ ] Note: don't try to master, focus on intuition

PRACTICE (1h):
[ ] RISC Zero hello world tutorial
    URL: https://dev.risczero.com/api/zkvm/quickstart
[ ] Just run their example, don't customize yet

COMMIT:
[ ] Commit: "learn: ZK book ch2-4 + RISC Zero hello world ran"
```

**W21 — FRIDAY 2026-10-02**

```
NETWORKING ACCELERATION (3h):
[ ] Apply to 5 small protocols / DeFi gigs (warm-up applications)
    Goal: get rejected fast, learn what's missing
    Use: Talent.io, web3.career, direct DMs
[ ] Track in Notion Job DB
[ ] Be specific: tailor each app to the company

COMMIT:
[ ] Commit: "docs: first 5 warm-up applications sent"
```

**W21 — SATURDAY 2026-10-03**

```
DEEP WORK (3h): ZK PROOF DEMO
[ ] RISC Zero: customize the hello world to verify a balance proof
    Use case: prove "I have at least X tokens" without revealing exact amount
[ ] Get it working off-chain first
[ ] Then verify on-chain in Solana program (use RISC Zero's verifier)

BLOG (1h):
[ ] Draft: "My First ZK Proof on Solana with RISC Zero"
```

**W21 — SUNDAY 2026-10-04**

```
[ ] W21 KPI
[ ] REST
```

**W21 DELIVERABLES:**
```
[ ] OSS PR submitted on major Solana repo (substantive)
[ ] First ZK proof demo with RISC Zero
[ ] 5 warm-up job applications sent
[ ] ZK book chapters 2-4 read
```

---

#### ◆ WEEK 22 (W22): 2026-10-05 → 2026-10-11
**Theme:** ZK proof project + apply pace increase

**W22 — MONDAY 2026-10-05**

```
BUILD (3h): ZK PROOF DEMO COMPLETION
[ ] Complete: balance threshold proof
    [ ] Off-chain: generate proof of "balance > X" without revealing balance
    [ ] On-chain: Solana program verifies proof using RISC Zero verifier
[ ] Use case scenario: private credit scoring
[ ] Add tests
[ ] Deploy verifier program to devnet

COMMIT:
[ ] Commit: "feat: zk_proof_demo balance threshold + on-chain verifier"
```

**W22 — TUESDAY 2026-10-06**

```
APPLY PACE (2h):
[ ] Send 5 more applications (target: 5/week through Phase 4)
[ ] Variations: 
    - 2 Solana-specific Backend Rust roles
    - 2 EVM+Rust hybrid roles
    - 1 stretch role (senior, may be too early but apply anyway)

LEARN (1h):
[ ] ZK book chapter 5

COMMIT:
[ ] Commit: "docs: 10 applications total sent, response tracking"
```

**W22 — WEDNESDAY 2026-10-07**

```
INTERVIEW PREP START (3h):
[ ] Read: Solana Cookbook end-to-end (refresh memory)
[ ] Practice explaining your projects out loud:
    Record yourself: 2-min pitch for each of 3 mainnet programs
    Listen back, refine
[ ] Common interview Q's research:
    [ ] "Walk me through your AMM architecture"
    [ ] "How does your lending handle liquidations"
    [ ] "What's a PDA and when do you use one"
    [ ] "Difference between Rust and TypeScript ownership"

COMMIT:
[ ] Commit: "practice: project pitches recorded + interview Q list"
```

**W22 — THURSDAY 2026-10-08**

```
PRACTICE (3h): RUST CODING INTERVIEWS
[ ] Solve 3 LeetCode Medium problems trong Rust:
    [ ] Problem 1: array/string
    [ ] Problem 2: tree/graph
    [ ] Problem 3: dynamic programming
[ ] Time yourself: target < 30 min each
[ ] Note Rust-specific patterns: ownership in recursive solutions, lifetime annotations

COMMIT:
[ ] Commit: "practice: 3 LeetCode Medium in Rust"
```

**W22 — FRIDAY 2026-10-09**

```
APPLY (1h):
[ ] Follow up on applications từ W21 (if no response after 5 days)
[ ] Send 2 more applications

REVIEW (2h):
[ ] Review ZK demo code
[ ] Add documentation
[ ] Write blog draft published next week

COMMIT:
[ ] Commit: "docs: ZK demo README + blog draft"
```

**W22 — SATURDAY 2026-10-10**

```
DEEP WORK (3h): SECOND OSS CONTRIBUTION
[ ] Pick another substantive issue
[ ] Implement
[ ] PR

BLOG (1h):
[ ] Publish ZK proof blog post
```

**W22 — SUNDAY 2026-10-11**

```
[ ] W22 KPI
[ ] REST
```

**W22 DELIVERABLES:**
```
[ ] ZK proof demo deployed devnet
[ ] 12+ applications sent total
[ ] OSS PR #5 submitted
[ ] 3 LeetCode Medium solved in Rust
[ ] Project pitches recorded
[ ] 1 ZK blog post published
```

---

#### ◆ WEEK 23 (W23): 2026-10-12 → 2026-10-18
**Theme:** Apply acceleration + first interviews

**W23 — MONDAY 2026-10-12**

```
APPLY (2h):
[ ] Tier 1 + Tier 2 companies: send 8 applications this week (heavier push)
[ ] Personalize each:
    - Reference specific recent product/blog
    - Link to relevant project
    - 2-3 sentence why you'd be a fit

LEARN (1h):
[ ] Practice system design Q: "Design a Solana DEX backend"
[ ] Outline: trade flow, indexing, settlement, MEV protection

COMMIT:
[ ] Commit: "docs: tier 1+2 applications + DEX system design notes"
```

**W23 — TUESDAY 2026-10-13**

```
INTERVIEW PREP (3h):
[ ] Common interview round structure research:
    [ ] Phone screen: 30 min, expect "tell me about your projects"
    [ ] Tech round 1: 60 min Rust coding (LeetCode Medium-Hard)
    [ ] Tech round 2: 60-90 min systems design
    [ ] Final/Onsite: 2-4 hour deep dive (Rust + DSA + system + culture)
[ ] Prepare for each round type với mock questions

COMMIT:
[ ] Commit: "docs: interview round prep notes"
```

**W23 — WEDNESDAY 2026-10-14**

```
MOCK INTERVIEW (2h):
[ ] Pramp.com — book free mock interview slot
[ ] OR: ask senior dev friend for 30-min mock
[ ] Topic: Rust coding round
[ ] Record session if possible
[ ] Take notes on what went well + gaps

COMMIT:
[ ] Commit: "practice: first mock interview recorded + notes"
```

**W23 — THURSDAY 2026-10-15**

```
REAL INTERVIEW (if any):
[ ] Check application responses — any phone screens scheduled?
[ ] If yes: prep the night before
[ ] If no: focus on outreach to follow-up

PRACTICE (3h):
[ ] LeetCode Medium x 3 in Rust
[ ] Specific topics: ownership tricky cases, lifetimes in algorithms

COMMIT:
[ ] Commit: "practice: 3 more LeetCode + interview prep"
```

**W23 — FRIDAY 2026-10-16**

```
APPLY + FOLLOW UP (2h):
[ ] Send 5 more applications (cumulative: 25+)
[ ] Follow up on stale applications (10+ days no response)
[ ] LinkedIn: connect with hiring managers from applied companies
    Custom note: "Hi [name], I recently applied for [role]. Just wanted to connect, big fan of [company's recent thing]."

LEARN (1h):
[ ] Read post-mortems của 3 famous DeFi exploits (Solana ecosystem)
[ ] Note: how were they detected, what could have prevented

COMMIT:
[ ] Commit: "docs: 25+ apps + 3 DeFi post-mortems studied"
```

**W23 — SATURDAY 2026-10-17**

```
DEEP WORK (4h): PORTFOLIO POLISH
[ ] Update portfolio dapp với latest:
    [ ] All 3 mainnet protocols showcased với live numbers
    [ ] ZK proof demo featured
    [ ] OSS contributions highlighted (PR links, status)
    [ ] Blog posts list (10+ now)
    [ ] Certifications (Solana Foundation Bootcamp, Encode Club, Otter Security)
    [ ] Skills matrix updated
[ ] Polish design: custom OG images, fast loading, mobile

COMMIT:
[ ] Commit: "feat: portfolio dapp polished cho Phase 3 apply phase"

BLOG (1h):
[ ] Draft: "Phase 2 Wrap: 6 Months of Rust + Solana"
```

**W23 — SUNDAY 2026-10-18**

```
[ ] W23 KPI
[ ] REST — long phase coming
```

**W23 DELIVERABLES:**
```
[ ] 25+ total applications sent
[ ] First mock interview done
[ ] First real phone screen (target, may not happen yet)
[ ] Portfolio dapp Phase-3 ready
[ ] 6+ LeetCode Medium solved trong Rust
[ ] 3 DeFi post-mortems studied
```

---

#### ◆ WEEK 24 (W24): 2026-10-19 → 2026-10-31
**Theme:** Q2 Decision Gate + Phase 3 prep
**Note:** W24 is extended (~12 days) to clean close M6 và Phase 2

**W24 — MONDAY 2026-10-19**

```
Q2 DECISION GATE EVALUATION (2h):
[ ] Run Q2 Gate checklist (see make-plan-protocols.md):
    
    GO criteria (must hit ≥ 6/8):
    [ ] 2+ mainnet protocols (have: 3) ✓
    [ ] 1+ OSS PR merged (count merged ones)
    [ ] 30+ active GitHub commits/month
    [ ] 1+ networking response (intro, DM reply, referral)
    [ ] Encode Club cert (have)
    [ ] Otter Security cert (have)
    [ ] Portfolio dapp live (have)
    [ ] 20+ applications sent (have ~25)
    
[ ] Record: GO / SLOW / NO-GO trong Notion Decision Gates DB
[ ] If GO: proceed Phase 3 confidently
[ ] If SLOW: identify gaps, dedicate W25 catchup
[ ] If NO-GO: trigger Plan B (pivot to Backend Rust + EVM only)

PUBLISH:
[ ] Phase 2 wrap blog post

COMMIT:
[ ] Commit: "milestone: Q2 Gate evaluation [RESULT]"
```

**W24 — TUESDAY 2026-10-20**

```
PHASE 3 PLANNING (3h):
[ ] Read make-plan-phase3.md (when written)
[ ] Identify: which projects continue, which sunset
[ ] Set Phase 3 quarterly goals trong Notion Phase Milestones
[ ] Pre-load: Phase 3 W25 daily entries trong Notion Daily Plan DB

COMMIT:
[ ] Commit: "docs: Phase 3 planning + Notion DB pre-loaded"
```

**W24 — WEDNESDAY 2026-10-21**

```
APPLY PUSH (3h):
[ ] Send 10 high-priority applications today
[ ] Tier 1 companies với personalized cover note
[ ] Track all carefully

NETWORKING (1h):
[ ] DM 3 senior engineers — sharing Phase 2 wrap post
[ ] Ask for referrals if you have rapport already

COMMIT:
[ ] Commit: "apply: 35+ total applications sent"
```

**W24 — THURSDAY 2026-10-22**

```
INTERVIEW IF SCHEDULED:
[ ] If phone screen: prep + execute
[ ] Record response (yes/no, feedback)

PRACTICE (3h):
[ ] LeetCode Hard x 1 trong Rust
[ ] System design: "Design a yield aggregator backend"

COMMIT:
[ ] Commit: "practice: LeetCode Hard + system design"
```

**W24 — FRIDAY 2026-10-23**

```
LEARN (3h):
[ ] Deep dive into Solana validator architecture
    Why: senior interviews ask infrastructure
[ ] Read: Solana whitepaper sections 4-6
[ ] Read: Anza's recent technical blog posts
[ ] Note key concepts: TPU, gulf stream, sealevel parallelism

COMMIT:
[ ] Commit: "docs: Solana validator architecture deep dive notes"
```

**W24 — SATURDAY 2026-10-24**

```
DEEP WORK (4h): RUST ADVANCED PATTERNS
[ ] Read Rust Book chapters 17-19 (advanced):
    [ ] Trait objects (dynamic dispatch)
    [ ] Pattern matching advanced
    [ ] Unsafe Rust (when và why)
    [ ] Macros (declarative + procedural intro)
[ ] Apply to your code: any place benefits from these?

COMMIT:
[ ] Commit: "learn: advanced Rust patterns applied to projects"
```

**W24 — SUNDAY 2026-10-25**

```
[ ] W24 KPI fill
[ ] REST
```

**W24 — MONDAY 2026-10-26**

```
INTERVIEW BLITZ (3h):
[ ] Apply to 5 more Tier 1 (cumulative: 40+)
[ ] Mock interview attempt #2 (record + analyze)
[ ] Practice talking through your mainnet programs để confident pitch

COMMIT:
[ ] Commit: "apply: 40+ apps + mock interview #2"
```

**W24 — TUESDAY 2026-10-27**

```
NETWORKING DEEP DIVE (3h):
[ ] Identify 5 internal referrer candidates (from your Twitter/Discord network)
[ ] Send personalized note asking for referral consideration
[ ] Approach: respect their time, offer something in return (testing their product, feedback)

COMMIT:
[ ] Commit: "network: 5 referral asks sent"
```

**W24 — WEDNESDAY 2026-10-28**

```
LEARN (3h):
[ ] Pick 1 advanced topic to differentiate:
    Option A: zkVM custom guest programs (RISC Zero deep)
    Option B: Solana program optimization (compute units)
    Option C: Cross-chain bridges (Wormhole or LayerZero)
[ ] Spend 3h going deep on chosen one

COMMIT:
[ ] Commit: "learn: deep dive on [chosen topic]"
```

**W24 — THURSDAY 2026-10-29**

```
INTERVIEW PREP REFINE (3h):
[ ] Collect feedback từ all interviews so far (or self-assess gaps)
[ ] Identify weakest area: coding speed, system design, communication
[ ] Spend 3h directly addressing weakest area

COMMIT:
[ ] Commit: "practice: targeted weakness improvement [area]"
```

**W24 — FRIDAY 2026-10-30**

```
PHASE 2 RETROSPECTIVE (3h):
[ ] Honest assessment:
    [ ] What did I overestimate (was easy)?
    [ ] What did I underestimate (was hard)?
    [ ] What surprised me?
    [ ] What would I tell W13 me?
[ ] Document trong RETRO_P2.md
[ ] Update LEARNING_LOG với 6-month summary

COMMIT:
[ ] Commit: "docs: Phase 2 retrospective"
```

**W24 — SATURDAY 2026-10-31**
> *Last day of Phase 2 — milestone tag*

```
PHASE 2 CLOSE (3h):
[ ] Tag GitHub: git tag v2.0-phase2-complete
[ ] Update karpathy-rust README với Phase 2 stats:
    - 3 mainnet protocols
    - 10+ tests, 80%+ coverage
    - 4-5 OSS PRs
    - 8+ blog posts
    - 40+ applications sent
    - 2 certifications (Encode + Otter)
    - 1 portfolio dapp
[ ] Twitter: "Phase 2 done. 6 months from Solidity-only to 3 mainnet protocols + audit cert + interviews started. Phase 3 starts tomorrow: deep ZK + landing offer. 🚀"

COMMIT:
[ ] Commit: "milestone: Phase 2 complete v2.0-phase2-complete"
```

**PHASE 2 FINAL DELIVERABLES CHECKLIST:**
```
MAINNET PROGRAMS:
[ ] amm_program — mainnet với verifiable build
[ ] lending_protocol — mainnet với verifiable build
[ ] yield_aggregator — mainnet với 3 strategies

DEMOS:
[ ] zk_proof_demo — devnet RISC Zero balance proof

TESTING:
[ ] All programs: 80%+ coverage
[ ] Integration test suites comprehensive

FRONTEND:
[ ] AMM frontend production
[ ] Lending frontend production
[ ] Yield vault frontend production
[ ] Portfolio dapp at portfolio.lehongvo.dev

OSS:
[ ] 4-5 PRs total (mix of trivial + substantive)
[ ] At least 1 substantive PR submitted/merged

CERTIFICATIONS:
[ ] Encode Club Solana Bootcamp ✅
[ ] Otter Security Audit ✅

PERSONAL BRAND:
[ ] Dev.to: 12+ posts total (Phase 1 + 2)
[ ] Twitter: 18+ threads
[ ] LinkedIn: updated, active
[ ] GitHub profile README polished

NETWORKING:
[ ] 15+ DMs to senior engineers
[ ] 5+ referral asks
[ ] Discord active (Anchor, Solana Tech, etc.)

JOB SEARCH:
[ ] 40+ applications sent
[ ] 1-3 phone screens completed
[ ] 0-1 onsite/tech rounds reached
[ ] 30-company target list active

INTERVIEW PREP:
[ ] 10+ LeetCode Medium in Rust
[ ] 1-2 LeetCode Hard
[ ] System design: 3 scenarios prepared
[ ] Mock interviews: 2+ done

LEARNING:
[ ] Rust Book chapters 17-19 (advanced)
[ ] ZK book chapters 1-5
[ ] RISC Zero hello world + custom guest
[ ] Solana validator architecture knowledge

HEALTH:
[ ] Buffer week observed (W19)
[ ] No major burnout episode
[ ] Commit streak: 80%+ weekdays
[ ] Mood average: 6+/10
```

---

## SECTION 4 SUMMARY: PHASE 2 STATS TARGETS

By end of W24 (2026-10-31), should have:

| Metric | Target | Realistic Floor |
|---|---|---|
| Mainnet protocols | 3 | 2 |
| OSS PRs submitted | 5 | 3 |
| OSS PRs merged | 2 | 1 |
| Total tests | 50+ | 30 |
| Blog posts (Phase 2) | 8 | 5 |
| Twitter threads | 12 | 8 |
| Applications sent | 40 | 25 |
| Phone screens | 3 | 1 |
| Tech rounds | 1 | 0 |
| Network touchpoints | 20 | 10 |
| Certifications | 2 | 2 |
| Buffer weeks observed | 2 (W19, W23 lighter) | 1 |
| Commit streak (weekdays) | 80%+ | 65%+ |
| Burnout episodes | 0 | 1 (recoverable) |

---

*Phase 2 file v1.0 | Aligned to make-plan.md (master + Phase 1) | Sync to Notion Daily Plan DB*
