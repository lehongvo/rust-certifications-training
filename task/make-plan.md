<!-- ============================================================
     AGENT EXECUTION PLAN — BLOCKCHAIN CAREER 2026–2027
     Version: 1.0 | Start: 2026-05-02 | End: 2027-04-30
     Owner: lehongvo | Repo: github.com/lehongvo/karpathy-rust
     ============================================================ -->

# 🤖 AGENT EXECUTION PLAN — BLOCKCHAIN CAREER 2026–2027

## ━━━ SECTION 0: AGENT INSTRUCTIONS ━━━

### 0.1 Cách đọc file này

```
Agent: Đây là kế hoạch chính xác theo ngày, tuần, tháng.
Mỗi ngày có tasks cụ thể với checkbox [ ].
Khi hoàn thành task, mark [x].
KHÔNG bỏ qua ngày nào — nếu không code được, ghi lý do vào DAILY LOG.
```

### 0.2 Quy tắc bất biến (HARD RULES — agent KHÔNG được bỏ qua)

```
RULE-01: Không có "zero commit day" — mỗi ngày phải có ít nhất 1 commit.
         Nếu không build được: commit note/doc/research là đủ.
RULE-02: Mỗi tuần có 1 ngày rest (Chủ Nhật). Không code, không đọc tech.
RULE-03: Mỗi tháng có 1 "buffer week" — chỉ refactor + review, không học mới.
RULE-04: Không apply job trước Week 27 (1/11/2026) trừ khi portfolio đạt Gate.
RULE-05: Mỗi project phải có README, tests, và deploy proof trước khi count.
RULE-06: Blog/Twitter content phải bằng tiếng Anh để build international brand.
RULE-07: Không ghi "Learning Rust" trên CV/LinkedIn cho đến khi có mainnet project.
RULE-08: Check Decision Gate cuối mỗi quý — nếu No-Go, trigger Plan B ngay.
```

### 0.3 Cấu trúc file

```
Section 0  : Agent Instructions (đọc trước)
Section 1  : Metadata & Tracking Setup
Section 2  : Daily Template (dùng mỗi ngày)
Section 3  : Phase 1 — Foundation (W1–W12 | May 2 – Jul 31, 2026)
Section 4  : Phase 2 — Build (W13–W24 | Aug 1 – Oct 31, 2026)
Section 5  : Phase 3 — Polish + ZK Intro (W25–W36 | Nov 1, 2026 – Jan 31, 2027)
Section 6  : Phase 4 — Interview Circuit (W37–W48 | Feb 1 – Apr 30, 2027)
Section 7  : Monthly Review Template
Section 8  : Decision Gates
Section 9  : Market Pulse Tracker (weekly check)
Section 10 : Emergency Protocols (Plan B / Plan C)
```

### 0.4 Định nghĩa mức độ hoàn thành task

```
[ ]  = Chưa làm
[~]  = Đang làm / Blocked
[x]  = Hoàn thành
[!]  = Skip có lý do (ghi lý do inline)
[>]  = Dời sang ngày khác (ghi ngày mới)
```

---

## ━━━ SECTION 1: METADATA & TRACKING SETUP ━━━

### 1.1 Profile

```yaml
name: lehongvo
start_date: 2026-05-02
target_date: 2027-04-30
target_salary: $5,000+/month (remote)
current_strengths:
  - Solidity (strong)
  - EVM internals (DeFi patterns, security)
  - Backend development
  - Web3.js / ethers.js
current_gaps:
  - Rust syntax & idioms
  - Solana account model + programs
  - Anchor framework
  - ZK primitives
  - Production Rust/Solana portfolio
repo: https://github.com/lehongvo/karpathy-rust
```

### 1.2 Setup Checklist (hoàn thành trước W1D1)

```
[ ] Cài Rust toolchain: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
[ ] Cài VS Code + rust-analyzer extension
[ ] Cài Solana CLI: sh -c "$(curl -sSfL https://release.solana.com/stable/install)"
[ ] Cài Anchor CLI: cargo install --git https://github.com/coral-xyz/anchor avm
[ ] Setup devnet wallet: solana-keygen new --outfile ~/.config/solana/id.json
[ ] Airdrop test SOL: solana airdrop 2 --url devnet
[ ] Fork repo karpathy-rust, setup README với learning log structure
[ ] Setup Twitter/X account với username @lehongvo_dev (hoặc tương tự)
[ ] Setup Dev.to account để publish blog
[ ] Tạo Notion/spreadsheet tracking: columns [Date | Task | Status | Notes | Commit]
[ ] Đăng ký Solana Foundation Developer Bootcamp (free): https://solana.com/developers
[ ] Bookmark: doc.rust-lang.org, anchor.so, solanacookbook.com, web3.career
```

### 1.3 Weekly KPI Tracker

```
Mỗi Chủ Nhật, record vào repo:
- Commits tuần này: ___
- Giờ code thực tế: ___/15-20h target
- Tasks completed: ___/___
- Blog/Twitter posts: ___
- Rust exercises done: ___
- Solana programs written: ___
- Applications sent (Phase 3+): ___
- Interview count (Phase 4+): ___
- Mood/burnout signal (1-10, 10=tốt): ___
```

---

## ━━━ SECTION 2: DAILY TEMPLATE ━━━

### Template — dùng mỗi ngày khi mở file

```markdown
### 📅 DATE: [YYYY-MM-DD] | WEEK: W[N] | DAY: D[N of week] | PHASE: [1/2/3/4]

**⏱ Time Budget:** [X]h available today

**☀️ MORNING (30 min — trước khi làm việc chính)**
- [ ] Đọc 1 article ngắn về Rust/Solana/Web3 (bookmark, đọc sau)
- [ ] Check Discord: Solana Tech, Anchor Framework (scan 5 phút, không rabbit hole)
- [ ] Mở tracking sheet, review task hôm nay

**🦀 DEEP WORK SESSION (Main task của ngày — xem Section 3/4/5/6)**
- [ ] [TASK CỤ THỂ THEO TUẦN]
- [ ] [TASK CỤ THỂ THEO TUẦN]

**🌙 EVENING (15 min — sau khi xong)**
- [ ] Git commit + push (minimum 1 commit)
- [ ] Update tracking sheet (status, notes, blockers)
- [ ] Write 2-3 sentences vào DAILY LOG trong repo

**📊 DAILY LOG ENTRY FORMAT:**
Date: [date] | Hours: [X] | Task: [what] | Blocker: [if any] | Tomorrow: [plan]
```

---

## ━━━ SECTION 3: PHASE 1 — FOUNDATION ━━━
**Duration:** Week 1–12 | 2026-05-02 → 2026-07-31  
**Goal:** Rust fluency đủ để viết Solana programs + Anchor basics  
**Success Criteria:** 3 Anchor programs deployed devnet, understand account model, daily commit streak

---

### ▶ MONTH 1 (M1): Rust Syntax + Solana Mental Model
**Calendar:** 2026-05-02 → 2026-05-31  
**Weekly Hours Target:** 15–20h (3–4h/weekday + 4–6h Saturday)

---

#### ◆ WEEK 1 (W1): 2026-05-02 → 2026-05-08
**Theme:** Setup + Rust Variables & Control Flow  
**Weekly Goal:** Environment ready, Rustlings ch1-ch3 done, repo seeded

**W1 — MONDAY 2026-05-05**
> *Hôm nay là ngày đầu tiên. Setup trước, code sau.*

```
SETUP (2h):
[ ] Chạy toàn bộ Setup Checklist từ Section 1.2
[ ] Tạo repo learning log: github.com/lehongvo/karpathy-rust/LEARNING_LOG.md
[ ] Thêm entry đầu tiên: ngày bắt đầu, mục tiêu, tâm trạng

LEARN (1.5h):
[ ] Đọc Rust Book Chapter 1: Getting Started
    URL: https://doc.rust-lang.org/book/ch01-00-getting-started.html
[ ] Chạy: cargo new hello_blockchain && cd hello_blockchain && cargo run
[ ] Đọc Rust Book Chapter 2: Guessing Game (full walkthrough)

COMMIT:
[ ] Commit: "chore: init learning repo, day 1 setup complete"
[ ] Twitter/X: "Day 1 of learning Rust for blockchain. Solidity dev making the switch. 🦀 #RustLang #Solana #buildinpublic"
```

**W1 — TUESDAY 2026-05-06**

```
LEARN (2h):
[ ] Rustlings — install: cargo install rustlings && rustlings init
[ ] Complete Rustlings: intro1, intro2 (warmup)
[ ] Complete Rustlings: variables1 → variables6 (all 6 exercises)
[ ] Read Rust Book Ch 3.1: Variables and Mutability
[ ] NOTE: So sánh mut keyword với Solidity's storage variables

PRACTICE (1h):
[ ] Viết mini program: declare 5 variables (string, int, bool, tuple, array)
[ ] Thêm vào hello_blockchain/src/types_demo.rs

COMMIT:
[ ] Commit: "feat: rustlings variables1-6 + types demo"
```

**W1 — WEDNESDAY 2026-05-07**

```
LEARN (2h):
[ ] Complete Rustlings: functions1 → functions5
[ ] Complete Rustlings: if1, if2 (control flow)
[ ] Read Rust Book Ch 3.3: Functions
[ ] Read Rust Book Ch 3.5: Control Flow

PRACTICE (1h):
[ ] Viết function: solana_fee_calculator(lamports: u64) -> f64 (convert lamports to SOL)
[ ] Add unit test: #[test] fn test_fee_calculator()

COMMIT:
[ ] Commit: "feat: rustlings functions + if + lamports calculator"
```

**W1 — THURSDAY 2026-05-08**

```
LEARN (2h):
[ ] Complete Rustlings: primitive_types1 → primitive_types6
[ ] Read Rust Book Ch 3.2: Data Types (integer, float, bool, char, tuple, array)
[ ] NOTE: Document trong LEARNING_LOG — primitive types vs Solidity types

PRACTICE (1h):
[ ] Viết program: parse Solana pubkey string thành bytes array [u8; 32]
[ ] Google: "Solana pubkey format explanation" — đọc 1 bài ngắn

COMMIT:
[ ] Commit: "feat: rustlings primitive_types + pubkey parser"
```

**W1 — FRIDAY 2026-05-09**

```
LEARN (2h):
[ ] Complete Rustlings: move_semantics1 → move_semantics5
[ ] Read Rust Book Ch 4.1: What is Ownership?
[ ] Read Rust Book Ch 4.2: References and Borrowing
[ ] CRITICAL NOTE: Ownership là concept quan trọng nhất. Dành thời gian.
    - Viết 3-5 ví dụ ownership trong LEARNING_LOG
    - So sánh: Solidity không có concept này vì storage là on-chain

COMMIT:
[ ] Commit: "feat: rustlings move_semantics + ownership notes"
```

**W1 — SATURDAY 2026-05-10**
> *Saturday = long session (4–6h)*

```
MORNING SESSION (2h):
[ ] Complete Rustlings: move_semantics6 (vibe_coding helper)
[ ] Complete Rustlings: structs1 → structs3
[ ] Read Rust Book Ch 5: Using Structs

AFTERNOON SESSION (2h):
[ ] Build Project: Solana Wallet Info CLI v0.1
    File: projects/wallet-cli/src/main.rs
    Feature: Accept pubkey as CLI arg, print formatted info
    Deps: use solana-client = "1.18" in Cargo.toml
    Steps:
    [ ] cargo new wallet-cli
    [ ] Add deps to Cargo.toml
    [ ] Implement: fn main() với std::env::args()
    [ ] Parse pubkey string
    [ ] Print: "Wallet: {pubkey} | Network: devnet"
    (Actual RPC call = Week 2)

BLOG (1h):
[ ] Write Dev.to draft: "Week 1: What a Solidity Dev Notices When Learning Rust"
    Key points:
    - Ownership vs storage (no GC, no implicit memory)
    - mut keyword vs Solidity's default mutability
    - Compiler errors are your friend
    - DON'T publish yet — review Sunday
```

**W1 — SUNDAY 2026-05-11**
> *REST DAY — Không code. Review only.*

```
REVIEW (30 min):
[ ] Review W1 KPI (Section 1.3) — fill in numbers
[ ] Read blog draft, edit for clarity
[ ] Scan Solana Discord headlines (5 min only)

REST:
[ ] Không mở VS Code
[ ] Không xem tutorial videos
[ ] Nghỉ ngơi thực sự
```

**W1 DELIVERABLES:**
```
[ ] Rustlings completed: intro(2), variables(6), functions(5), if(2), primitive_types(6), move_semantics(6), structs(3) = 30 exercises
[ ] 1 Rust project scaffolded (wallet-cli)
[ ] 1 blog draft written
[ ] Commit streak: 5/5 weekdays
[ ] Twitter: 1 post
```

---

#### ◆ WEEK 2 (W2): 2026-05-12 → 2026-05-18
**Theme:** Enums, Error Handling, Ownership Deep Dive  
**Weekly Goal:** Rustlings ch4-ch7 done, first real Solana RPC call

**W2 — MONDAY 2026-05-12**

```
LEARN (2h):
[ ] Complete Rustlings: enums1 → enums3
[ ] Read Rust Book Ch 6: Enums and Pattern Matching
[ ] NOTE: Option<T> và Result<T,E> là "everyday Rust" — memorize patterns

PRACTICE (1h):
[ ] Add to wallet-cli: use Result<> for error handling
[ ] Replace panic!() với proper error returns

COMMIT:
[ ] Publish W1 blog post lên Dev.to (edited version)
[ ] Commit: "feat: wallet-cli error handling with Result<>"
```

**W2 — TUESDAY 2026-05-13**

```
LEARN (2h):
[ ] Complete Rustlings: strings1 → strings4
[ ] Complete Rustlings: hashmaps1 → hashmaps3
[ ] Read Rust Book Ch 8: Common Collections (String, Vec, HashMap)
[ ] NOTE: String vs &str — viết ví dụ cụ thể cho từng case

PRACTICE (1h):
[ ] Viết: HashMap để map token symbols → contract addresses (Solana SPL tokens)
[ ] Print formatted table ra stdout

COMMIT:
[ ] Commit: "feat: rustlings strings+hashmaps + SPL token map demo"
```

**W2 — WEDNESDAY 2026-05-14**

```
LEARN (2h):
[ ] Complete Rustlings: error_handling1 → error_handling3
[ ] Read Rust Book Ch 9: Error Handling (unwrap, expect, ?, custom errors)
[ ] NOTE: ? operator = game changer, như Promise.then() nhưng synchronous

PRACTICE (1h):
[ ] Add Solana RPC call to wallet-cli:
    - Add dep: solana-client
    - Call: RpcClient::new("https://api.devnet.solana.com")
    - get_balance(pubkey) → print in SOL
    - Handle network error với proper Result<>

COMMIT:
[ ] Commit: "feat: wallet-cli first RPC call — get devnet balance"
```

**W2 — THURSDAY 2026-05-15**

```
LEARN (2h):
[ ] Complete Rustlings: generics1 → generics2
[ ] Complete Rustlings: traits1 → traits5
[ ] Read Rust Book Ch 10.1: Generic Data Types
[ ] Read Rust Book Ch 10.2: Traits

PRACTICE (1h):
[ ] Viết generic function: fn print_info<T: std::fmt::Display>(label: &str, value: T)
[ ] Implement Display trait cho custom struct WalletInfo

COMMIT:
[ ] Commit: "feat: rustlings generics+traits + WalletInfo Display impl"
```

**W2 — FRIDAY 2026-05-16**

```
LEARN (2h):
[ ] Complete Rustlings: lifetimes1 → lifetimes3
[ ] Read Rust Book Ch 10.3: Lifetimes
[ ] NOTE: Lifetimes là hardest concept cho người mới. Đừng panic.
          Rule of thumb: "lifetime = how long a reference is valid"
          Viết 3 examples trong LEARNING_LOG

PRACTICE (1h):
[ ] wallet-cli: refactor để pass &str thay vì String where possible
[ ] clippy: run `cargo clippy` và fix all warnings

COMMIT:
[ ] Commit: "refactor: wallet-cli lifetime annotations + clippy clean"
```

**W2 — SATURDAY 2026-05-17**

```
DEEP WORK (3h):
[ ] Read Solana Docs: Programming Model Overview
    URL: https://solana.com/docs/core/accounts
    Topics:
    [ ] Account model: data, lamports, owner, executable
    [ ] Programs vs Accounts distinction
    [ ] Transaction structure
    [ ] Instruction format
[ ] Take notes in LEARNING_LOG: "Solana vs Ethereum mental model diff"
    Table format:
    | Concept | Ethereum | Solana |
    | Smart Contract | Contract account with code+storage | Program account (stateless) |
    | State | In contract | In separate data accounts |
    | "Constructor" | constructor() | init instruction |

PRACTICE (1h):
[ ] Complete Rustlings: iterators1 → iterators3
[ ] Add to wallet-cli: list multiple wallets from a Vec<Pubkey>

BLOG (1h):
[ ] Write Twitter thread draft: "Solana vs Ethereum for EVM devs — 5 mental model shifts"
    Thread outline:
    1. Programs are stateless (shocking to Solidity devs)
    2. State lives in accounts, not contracts
    3. No constructor — use init instruction
    4. Everything is an account (your wallet, the program, the data)
    5. PDAs = "deterministic contract addresses"
```

**W2 — SUNDAY 2026-05-18**

```
REVIEW (30 min):
[ ] W2 KPI fill
[ ] Publish Twitter thread (5 tweets with diagrams drawn in ASCII)
[ ] Plan W3 — review what's blocked

REST:
[ ] No code. Seriously.
```

**W2 DELIVERABLES:**
```
[ ] Rustlings: enums(3), strings(4), hashmaps(3), error_handling(3), generics(2), traits(5), lifetimes(3), iterators(3) = 26 more exercises (total: 56)
[ ] wallet-cli: RPC call working, balance fetch from devnet
[ ] 1 blog post published (Dev.to)
[ ] 1 Twitter thread published
[ ] Commit streak: 5/5
```

---

#### ◆ WEEK 3 (W3): 2026-05-19 → 2026-05-25
**Theme:** Closures, Async/Await, Tokio — then Hello Solana Program  
**Weekly Goal:** Rustlings complete, first native Rust Solana program deployed to devnet

**W3 — MONDAY 2026-05-19**

```
LEARN (2h):
[ ] Complete Rustlings: closures1 → closures3
[ ] Read Rust Book Ch 13.1: Closures
[ ] NOTE: Closures in Rust ≈ lambdas/arrow functions pero con ownership rules

PRACTICE (1h):
[ ] wallet-cli: use closure + iterator to filter wallets by balance threshold
    fn wallets_above_threshold(wallets: &[WalletInfo], threshold: u64) -> Vec<&WalletInfo>

COMMIT:
[ ] Commit: "feat: rustlings closures + wallet filter closure"
```

**W3 — TUESDAY 2026-05-20**

```
LEARN (2h):
[ ] Complete Rustlings: threads1 → threads3
[ ] Read Rust Book Ch 16.1: Threads
[ ] Read intro to Tokio: https://tokio.rs/tokio/tutorial (ch1: Hello Tokio only)
[ ] NOTE: async/await in Rust = same pattern as JS but compiler-enforced

PRACTICE (1h):
[ ] wallet-cli: make RPC call async với tokio
    #[tokio::main] async fn main()
    Add dep: tokio = { version = "1", features = ["full"] }

COMMIT:
[ ] Commit: "feat: wallet-cli async/await with tokio"
```

**W3 — WEDNESDAY 2026-05-21**

```
LEARN (2h):
[ ] Complete Rustlings: smart_pointers1 → smart_pointers4
[ ] Read Rust Book Ch 15.1: Box<T>
[ ] Read Rust Book Ch 15.4: Rc<T>
[ ] NOTE: Box<T> = heap allocation. In Solana programs: rarely used directly.

LEARN (1h):
[ ] Read Solana Docs: Writing Programs in Rust (native, no Anchor)
    URL: https://solana.com/docs/programs/rust
    Focus: entrypoint!, process_instruction, AccountInfo struct

COMMIT:
[ ] Commit: "feat: rustlings smart_pointers + solana program structure notes"
```

**W3 — THURSDAY 2026-05-22**

```
BUILD (3h): FIRST SOLANA PROGRAM — Native Rust (no Anchor)
[ ] cargo new --lib solana-hello-native
[ ] Add to Cargo.toml:
    [lib]
    crate-type = ["cdylib", "lib"]
    [dependencies]
    solana-program = "1.18"
[ ] Implement in src/lib.rs:
    use solana_program::{
        account_info::AccountInfo, entrypoint, entrypoint::ProgramResult,
        pubkey::Pubkey, msg,
    };
    entrypoint!(process_instruction);
    pub fn process_instruction(
        program_id: &Pubkey,
        accounts: &[AccountInfo],
        instruction_data: &[u8],
    ) -> ProgramResult {
        msg!("Hello from lehongvo's first Solana program!");
        msg!("Program ID: {}", program_id);
        Ok(())
    }
[ ] cargo build-bpf (phải có solana-bpf toolchain)
[ ] solana program deploy target/deploy/solana_hello_native.so --url devnet
[ ] Record Program ID in LEARNING_LOG

COMMIT:
[ ] Commit: "feat: first native Solana program deployed to devnet 🎉"
[ ] Twitter: "Just deployed my first Solana program (native Rust)! Program ID: [ID] on devnet. No Anchor yet — understanding the bare metal first. 🦀 #Solana #Rust"
```

**W3 — FRIDAY 2026-05-23**

```
LEARN (2h):
[ ] Complete Rustlings: macros1 → macros4
[ ] Read: What is the entrypoint! macro? (source code, 30 min)
[ ] Read Solana Docs: Transaction Anatomy
    URL: https://solana.com/docs/core/transactions

PRACTICE (1h):
[ ] Write client script (TypeScript) to call hello program:
    - npm init, install @solana/web3.js
    - Send transaction to hello program
    - Confirm and print logs
[ ] Run: solana logs --url devnet [PROGRAM_ID]

COMMIT:
[ ] Commit: "feat: TypeScript client for hello native program"
```

**W3 — SATURDAY 2026-05-24**

```
RUSTLINGS COMPLETION (2h):
[ ] Complete remaining Rustlings exercises:
    [ ] type_conversions: try_from_into (3 exercises)
    [ ] standard_library_types: box1, arc1, cow1 (3 exercises)
    [ ] tests: tests1-4 (4 exercises)
    [ ] quiz1, quiz2, quiz3 (3 exercises)
[ ] RUN: rustlings verify (all should pass)
[ ] Screenshot "All exercises done!" → save to repo assets/rustlings-complete.png

REVIEW (1h):
[ ] Review all LEARNING_LOG notes from W1-W3
[ ] Identify: top 3 Rust concepts still unclear
[ ] Google each one, add clarification note

BLOG (1h):
[ ] Write Dev.to post: "I Deployed My First Solana Program (Without Anchor)"
    Include: program ID, what msg!() does, how entrypoint! macro works,
             comparison to Solidity contract deployment
```

**W3 — SUNDAY 2026-05-25**

```
REVIEW (30 min):
[ ] W3 KPI + Month 1 partial review
[ ] Publish Dev.to blog post
[ ] REST
```

**W3 DELIVERABLES:**
```
[ ] Rustlings: 100% complete (all exercises)
[ ] First native Rust Solana program deployed devnet — Program ID recorded
[ ] TypeScript client that calls the program
[ ] 1 blog post published
[ ] 1 Twitter post with program ID
[ ] Commit streak: 5/5
```

---

#### ◆ WEEK 4 (W4): 2026-05-26 → 2026-06-01
**Theme:** Anchor Framework Intro + Counter Program  
**Weekly Goal:** First Anchor program deployed devnet, understand Anchor macros

**W4 — MONDAY 2026-05-26**

```
SETUP (1h):
[ ] Install Anchor via AVM: avm install latest && avm use latest
[ ] Verify: anchor --version
[ ] Read Anchor Book Chapter 1: Introduction
    URL: https://book.anchor-lang.com/introduction/introduction.html
[ ] Read: Why Anchor? (vs native Rust Solana)

LEARN (1h):
[ ] Read Anchor Book Chapter 2: Getting Started
[ ] anchor init counter_program
[ ] Examine generated project structure:
    - programs/counter_program/src/lib.rs (program)
    - tests/counter_program.ts (test)
    - Anchor.toml (config)
    - migrations/deploy.ts

COMMIT:
[ ] Commit: "chore: anchor counter_program scaffold"
```

**W4 — TUESDAY 2026-05-27**

```
BUILD (3h): ANCHOR COUNTER PROGRAM
[ ] Implement in programs/counter_program/src/lib.rs:

use anchor_lang::prelude::*;
declare_id!("YOUR_PROGRAM_ID");

#[program]
pub mod counter_program {
    use super::*;
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let counter = &mut ctx.accounts.counter;
        counter.authority = ctx.accounts.user.key();
        counter.count = 0;
        msg!("Counter initialized at 0");
        Ok(())
    }
    pub fn increment(ctx: Context<CounterOp>) -> Result<()> {
        let counter = &mut ctx.accounts.counter;
        counter.count = counter.count.checked_add(1)
            .ok_or(ErrorCode::Overflow)?;
        msg!("Counter incremented to {}", counter.count);
        Ok(())
    }
    pub fn decrement(ctx: Context<CounterOp>) -> Result<()> {
        let counter = &mut ctx.accounts.counter;
        counter.count = counter.count.checked_sub(1)
            .ok_or(ErrorCode::Underflow)?;
        msg!("Counter decremented to {}", counter.count);
        Ok(())
    }
    pub fn reset(ctx: Context<CounterOp>) -> Result<()> {
        let counter = &mut ctx.accounts.counter;
        counter.count = 0;
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 32 + 8)]
    pub counter: Account<'info, Counter>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct CounterOp<'info> {
    #[account(mut, has_one = authority)]
    pub counter: Account<'info, Counter>,
    pub authority: Signer<'info>,
}

#[account]
pub struct Counter {
    pub authority: Pubkey,
    pub count: u64,
}

#[error_code]
pub enum ErrorCode {
    #[msg("Counter overflow")]
    Overflow,
    #[msg("Counter underflow")]
    Underflow,
}

[ ] anchor build (should succeed)
[ ] anchor deploy --provider.cluster devnet
[ ] Record Program ID

COMMIT:
[ ] Commit: "feat: anchor counter program with init/increment/decrement/reset"
```

**W4 — WEDNESDAY 2026-05-28**

```
TEST (2h): ANCHOR COUNTER TESTS
[ ] Implement TypeScript tests in tests/counter_program.ts:
    [ ] Test: initialize counter, verify count = 0
    [ ] Test: increment 3 times, verify count = 3
    [ ] Test: decrement, verify count = 2
    [ ] Test: reset, verify count = 0
    [ ] Test: decrement below 0 → expect error
    [ ] Test: non-authority increment → expect error
[ ] Run: anchor test (all tests should pass)
[ ] Fix failures, re-run until 100% pass

COMMIT:
[ ] Commit: "test: counter program 6/6 tests passing"
```

**W4 — THURSDAY 2026-05-29**

```
LEARN (2h):
[ ] Read Anchor Book Chapter 3: PDAs (Program Derived Addresses)
    URL: https://book.anchor-lang.com/anchor_in_depth/PDAs.html
[ ] NOTE in LEARNING_LOG:
    - PDA = address derived from seeds + program_id, no private key
    - EVM equivalent: CREATE2 deterministic address
    - Usage: user-specific data accounts without storing their addresses

PRACTICE (1h):
[ ] Add PDA to counter program:
    - Derive counter PDA from user's pubkey + "counter" seed
    - Update Initialize struct to use PDA seeds
    - Update test to use PDA addresses
[ ] anchor build && anchor test

COMMIT:
[ ] Commit: "feat: counter program uses PDA for deterministic account address"
```

**W4 — FRIDAY 2026-05-30**

```
LEARN (1h):
[ ] Read Anchor Book Chapter 4: Cross-Program Invocations (CPI)
    (Read only, no implementation yet)
[ ] Read: Solana Cookbook — Accounts
    URL: https://solanacookbook.com/core-concepts/accounts.html

REVIEW (1h):
[ ] Review entire counter_program code
[ ] Add inline comments explaining every macro: #[program], #[account], #[derive(Accounts)]
[ ] Run cargo clippy -- -D warnings (fix all)
[ ] Write LEARNING_LOG entry: "What I understand about Anchor macros"

COMMIT:
[ ] Commit: "docs: inline comments + clippy clean for counter_program"
```

**W4 — SATURDAY 2026-05-31**
> *Last day of May — M1 completion check*

```
BUFFER DAY (2h):
[ ] Review ALL M1 progress
[ ] Update repo README with: projects built, programs deployed, links
[ ] Ensure LEARNING_LOG has entries for every significant concept

BLOG (2h):
[ ] Write Dev.to: "Month 1 Complete: From Solidity to Anchor — What Surprised Me"
    Include:
    - Anchor macros demystified (what each does)
    - The PDA mental model vs CREATE2
    - Ownership in Solana programs vs Solidity storage
    - Counter program GitHub link + devnet Program ID

TWITTER (30 min):
[ ] Post: "Completed Month 1 of my Rust/Solana journey! Stats:
    ✅ Rustlings: 100% complete
    ✅ 2 Solana programs deployed (native + Anchor)  
    ✅ Anchor macros understood
    ✅ Blog: 2 posts published
    Next: SPL Tokens + DeFi primitives 🚀
    #Solana #Rust #buildinpublic"
```

**W4 — SUNDAY 2026-06-01**

```
REVIEW (45 min):
[ ] M1 KPI Summary:
    - Rustlings complete: Y/N
    - Programs deployed: __ / target 2
    - Blog posts: __ / target 2
    - Twitter posts: __ / target 3
    - Commit streak: __/20 weekdays
    - Hours invested: __ / 60-80h target
[ ] Decision: Am I on track? (Y/Slow/Behind)
[ ] Set M2 priorities based on gaps
```

**W4 DELIVERABLES:**
```
[ ] Anchor Counter program deployed devnet (with PDA)
[ ] 6/6 tests passing
[ ] 1 blog post (Dev.to) — Month 1 retrospective
[ ] M1 KPI summary completed
[ ] Commit streak: 5/5 this week
```

---

### ▶ MONTH 2 (M2): Anchor Deep Dive + Solana Foundation Bootcamp
**Calendar:** 2026-06-01 → 2026-06-30  
**Weekly Hours Target:** 15–20h  
**Key Events:** Encode Club Solana Bootcamp starts June 2 (FREE — register NOW)

---

#### ◆ WEEK 5 (W5): 2026-06-01 → 2026-06-07
**Theme:** SPL Tokens + Solana Foundation Bootcamp kickoff

**W5 — MONDAY 2026-06-02**

```
ADMIN (30 min):
[ ] Register Encode Club Solana Bootcamp (cohort June 2 – July 17)
    URL: https://www.encodeclub.com/solana-bootcamp
    FREE — no cost, register immediately
[ ] Join bootcamp Discord channel

LEARN (2h):
[ ] Read Solana Cookbook: SPL Tokens
    URL: https://solanacookbook.com/references/token.html
[ ] Topics: Token mint, Token account, ATA (Associated Token Account)
[ ] NOTE: SPL Token = ERC-20 equivalent, but as a separate program you CPI into
[ ] Read: Token-2022 overview (new features vs classic SPL)

COMMIT:
[ ] Commit: "docs: SPL token notes + ATA mental model"
```

**W5 — TUESDAY 2026-06-03**

```
BUILD (3h): SPL TOKEN MINT PROGRAM
[ ] anchor init token_manager
[ ] Implement:
    [ ] create_mint instruction: create SPL token mint with authority
    [ ] mint_tokens instruction: mint N tokens to a recipient ATA
    [ ] burn_tokens instruction: burn tokens from sender
[ ] Add deps:
    spl-token = "4.0"
    anchor-spl = "0.29"
[ ] Required imports: use anchor_spl::token::{self, Token, TokenAccount, Mint}

COMMIT:
[ ] Commit: "feat: SPL token mint/burn program v0.1"
```

**W5 — WEDNESDAY 2026-06-04**

```
BUILD CONTINUE (2h):
[ ] Add tests for token_manager:
    [ ] Test: create_mint → verify mint authority
    [ ] Test: mint 1000 tokens → check ATA balance
    [ ] Test: burn 500 tokens → check balance reduced
[ ] anchor test (all passing)
[ ] Deploy to devnet: anchor deploy --provider.cluster devnet

BOOTCAMP (1h):
[ ] Follow Encode Club Session 1 materials (uploaded to Discord)
[ ] Take notes in LEARNING_LOG

COMMIT:
[ ] Commit: "test: token_manager 3/3 tests passing + devnet deploy"
```

**W5 — THURSDAY 2026-06-05**

```
LEARN (2h):
[ ] Read Anchor Book: Account Constraints (full list)
    URL: https://book.anchor-lang.com/anchor_references/account-constraints.html
    Study each constraint:
    [ ] init, init_if_needed
    [ ] mut, has_one, constraint
    [ ] seeds, bump (PDA)
    [ ] token::mint, token::authority
    [ ] close (account closure + lamport recovery)

PRACTICE (1h):
[ ] Add to token_manager: close_mint_authority instruction
    Use: #[account(mut, close = authority)]
[ ] Test the close functionality

COMMIT:
[ ] Commit: "feat: token_manager add close account constraint"
```

**W5 — FRIDAY 2026-06-06**

```
LEARN (2h):
[ ] Read: Solana Security — Common Vulnerabilities
    URL: https://github.com/coral-xyz/sealevel-attacks (read all 9 attacks)
    Attacks:
    [ ] 1. Signer Authorization
    [ ] 2. Account Data Matching  
    [ ] 3. Owner Checks
    [ ] 4. Type Cosplay
    [ ] 5. Arbitrary CPI
    [ ] 6. Duplicate Mutable Accounts
    [ ] 7. Bump Seed Canonicalization
    [ ] 8. Reinitialization Attacks
    [ ] 9. Loss of Precision

NOTE (1h):
[ ] For each attack: write 1 paragraph in LEARNING_LOG
    Format: Attack name | What it is | Solidity equivalent | Anchor mitigation

COMMIT:
[ ] Commit: "docs: Solana security 9 attacks notes with EVM comparison"
[ ] Twitter: "Just read through all 9 Sealevel attacks on Solana. As a Solidity dev, some are familiar (reentrancy-like) but others are unique to the account model. Key takeaway: always validate account owners. Thread soon. 🔐 #SolanaSecurity"
```

**W5 — SATURDAY 2026-06-07**

```
DEEP WORK (4h):
[ ] Build: Voting Program (new project, demonstrates real-world pattern)
    anchor init voting_program
    Features:
    [ ] create_proposal(title: String, description: String, end_time: i64)
    [ ] vote(proposal: Pubkey, vote_type: VoteType) — enum: { Yes, No, Abstain }
    [ ] close_proposal(proposal: Pubkey) — tallies results
    Accounts:
    [ ] Proposal { title, description, yes_votes, no_votes, abstain, end_time, status, authority }
    [ ] VoteRecord { voter, proposal, vote_type } — PDA from [voter, proposal]
    Security: VoteRecord PDA prevents double voting

BLOG:
[ ] Write Twitter thread: "Solana's 9 Security Attack Vectors (with EVM comparison)"
    5-7 tweets, one attack per tweet with code snippet
```

**W5 — SUNDAY 2026-06-08**
```
[ ] W5 KPI fill
[ ] Publish Twitter thread
[ ] REST
```

---

#### ◆ WEEK 6 (W6): 2026-06-08 → 2026-06-14
**Theme:** Voting Program completion + Solana Foundation Bootcamp Week 2

**W6 — MONDAY 2026-06-09**

```
BUILD (3h): VOTING PROGRAM COMPLETE
[ ] Finish voting_program implementation from W5 Saturday
[ ] Add comprehensive tests:
    [ ] create_proposal → verify fields
    [ ] vote Yes twice from same wallet → expect error (double vote protection)
    [ ] vote from 3 different wallets, close → verify tally
    [ ] vote after end_time → expect error
[ ] anchor test (4/4 passing)
[ ] Deploy devnet

COMMIT:
[ ] Commit: "feat: voting program complete + 4/4 tests + devnet deploy"
```

**W6 — TUESDAY 2026-06-10**

```
LEARN (2h):
[ ] Solana Foundation Bootcamp materials (week 2)
[ ] Read: Token-2022 Extensions
    URL: https://spl.solana.com/token-2022/extensions
    Focus: TransferFee, NonTransferable, PermanentDelegate
[ ] NOTE: Token-2022 = ERC-20 with built-in extensions (vs OpenZeppelin separate contracts)

PRACTICE (1h):
[ ] Add Token-2022 support to token_manager:
    - Use spl-token-2022 crate
    - Implement: create_mint_with_transfer_fee (5% fee)

COMMIT:
[ ] Commit: "feat: token_manager Token-2022 transfer fee extension"
```

**W6 — WEDNESDAY 2026-06-11**

```
LEARN (2h):
[ ] Read: Metaplex Docs — Token Metadata Standard
    URL: https://developers.metaplex.com/token-metadata
[ ] Topics: Metadata Account, Master Edition, collection
[ ] NOTE: Metaplex = NFT standard on Solana. Like ERC-721 but different account structure.

PRACTICE (1h):
[ ] Extend token_manager: add_metadata instruction
    CPI to Metaplex Token Metadata program
    Fields: name, symbol, uri (IPFS link)

COMMIT:
[ ] Commit: "feat: token_manager + metaplex metadata CPI"
```

**W6 — THURSDAY 2026-06-12**

```
LEARN (2h):
[ ] Read: Solana Cookbook — Cross-Program Invocations (CPI)
    URL: https://solanacookbook.com/references/programs.html#cross-program-invocations
[ ] Understand: invoke() vs invoke_signed() (for PDAs)
[ ] CRITICAL: invoke_signed = when your program's PDA needs to sign

PRACTICE (1h):
[ ] Create mini-demo: escrow that CPIs to SPL Token program
    [ ] Lock tokens in escrow account
    [ ] Release to recipient using invoke_signed (PDA authority)

COMMIT:
[ ] Commit: "feat: CPI demo with invoke_signed for PDA authority"
```

**W6 — FRIDAY 2026-06-13**

```
REVIEW DAY (3h):
[ ] Review all 3 programs: counter, token_manager, voting_program
[ ] For each program:
    [ ] README.md: architecture description, account diagrams, deploy info
    [ ] All tests passing
    [ ] No clippy warnings
    [ ] Security: check each against Sealevel 9 attacks list
[ ] Update karpathy-rust main README: project index with links

COMMIT:
[ ] Commit: "docs: READMEs for all 3 programs + main index"
```

**W6 — SATURDAY 2026-06-14**

```
BLOG (2h):
[ ] Write Dev.to post: "Building a Double-Vote-Proof Voting System on Solana"
    Include: PDA for VoteRecord, how bump seed prevents double-vote,
             code snippets, test results, devnet links

LEARN (2h):
[ ] Read Solana Cookbook: Staking
    URL: https://solanacookbook.com/references/staking.html
[ ] Preview M3 material: basic staking mechanics (prepare for next month)
```

**W6 — SUNDAY 2026-06-15**
```
[ ] W6 KPI
[ ] Publish blog post
[ ] REST
```

---

#### ◆ WEEK 7 (W7): 2026-06-15 → 2026-06-21
**Theme:** Staking Contract + Async Rust deep dive

**W7 — MONDAY 2026-06-16**

```
BUILD (3h): BASIC STAKING PROGRAM
anchor init staking_program

Implement:
[ ] stake(amount: u64) — transfer SPL tokens to vault PDA
[ ] unstake(amount: u64) — return tokens + accrued rewards
[ ] claim_rewards() — claim pending rewards without unstaking
[ ] Accounts:
    StakePool { authority, token_mint, vault, reward_rate, total_staked }
    StakeRecord { owner, amount, start_time, rewards_claimed } (PDA from [owner])
[ ] Reward formula: rewards = amount * rate * (current_time - start_time) / SECONDS_PER_DAY

COMMIT:
[ ] Commit: "feat: staking program scaffold + account definitions"
```

**W7 — TUESDAY 2026-06-17**

```
BUILD CONTINUE (3h):
[ ] Implement stake() and unstake() instructions
[ ] Handle: fractional rewards (use u64 math, avoid f64 in programs)
[ ] Add authority checks for unstake
[ ] Add: cannot unstake more than staked
[ ] Write tests:
    [ ] stake 100 tokens
    [ ] wait (mock time using Clock sysvar)
    [ ] claim_rewards
    [ ] unstake

COMMIT:
[ ] Commit: "feat: staking stake/unstake/rewards logic + time-based calc"
```

**W7 — WEDNESDAY 2026-06-18**

```
BUILD TESTS + SECURITY (2h):
[ ] Complete staking tests (all scenarios)
[ ] Security review:
    [ ] Verify cannot claim_rewards before staking
    [ ] Verify cannot unstake other user's stake
    [ ] Verify overflow protection on reward calc
[ ] Run anchor test — fix until all pass
[ ] Deploy to devnet

BOOTCAMP (1h):
[ ] Solana Foundation Bootcamp: Week 3 material

COMMIT:
[ ] Commit: "test: staking program complete tests + security hardening"
```

**W7 — THURSDAY 2026-06-19**

```
LEARN (2h):
[ ] Async Rust deep dive: tokio advanced
    URL: https://tokio.rs/tokio/tutorial (chapters 2-5)
    Topics: Spawning tasks, channels (mpsc), select!, timeout
[ ] Build: async Solana indexer (reads on-chain data continuously)
    while true: fetch_slot → compare with last_slot → print new txns

PRACTICE (1h):
[ ] Add to wallet-cli: async balance monitor
    Poll every 5s, print when balance changes

COMMIT:
[ ] Commit: "feat: async Solana balance monitor with tokio"
```

**W7 — FRIDAY 2026-06-20**

```
LEARN (2h):
[ ] Read: Anchor Book — Events
    URL: https://book.anchor-lang.com/anchor_in_depth/events.html
[ ] Add events to staking_program:
    #[event] struct Staked { user: Pubkey, amount: u64, timestamp: i64 }
    #[event] struct Unstaked { user: Pubkey, amount: u64, rewards: u64 }
[ ] Emit events in stake() and unstake()
[ ] Update tests to check event emission

COMMIT:
[ ] Commit: "feat: staking program emit Staked/Unstaked events"
```

**W7 — SATURDAY 2026-06-21**

```
DEEP WORK (4h):
[ ] Read: RareSkills "Solana Course" (free online version)
    URL: https://www.rareskills.io/solana-tutorial
    Complete: Chapter 1-5 (account model, instructions, PDAs, CPI, SPL)
[ ] NOTE discrepancies vs official docs in LEARNING_LOG

BLOG:
[ ] Write Dev.to: "Building a Token Staking Program on Solana (with Reward Math)"
    Focus: fixed-point arithmetic, Clock sysvar, PDA vault design
```

**W7 — SUNDAY 2026-06-22**
```
[ ] W7 KPI
[ ] Publish blog
[ ] REST
```

---

#### ◆ WEEK 8 (W8): 2026-06-22 → 2026-06-30
**Theme:** M2 Wrap-up + OSS Contribution + Solana Bootcamp cert  
**Note:** W8 is slightly longer (9 days, ends Jun 30 for clean M2 close)

**W8 — MONDAY 2026-06-23**

```
OSS CONTRIBUTION (3h):
[ ] Browse Anchor GitHub issues: https://github.com/coral-xyz/anchor/issues
    Filter: "good first issue" or "documentation"
[ ] Pick 1 achievable issue (doc improvement, typo fix, test addition)
[ ] Fork anchor repo, create branch: fix/[issue-title]
[ ] Implement fix + test
[ ] Submit PR

COMMIT:
[ ] Commit in your fork + submit PR
[ ] Record in LEARNING_LOG: "First OSS PR: [issue title] [PR link]"
```

**W8 — TUESDAY 2026-06-24**

```
REVIEW + SOLIDIFY (3h):
[ ] Review all M2 programs: token_manager, voting_program, staking_program
[ ] Create architecture diagrams (ASCII or draw.io):
    For staking_program: show StakePool → StakeRecord PDA relationship
[ ] Verify all programs:
    [ ] Deployed on devnet with verifiable build
    [ ] All tests passing
    [ ] Security hardened (Sealevel 9 checklist)
    [ ] README complete with: description, architecture, deploy info, usage

COMMIT:
[ ] Commit: "docs: architecture diagrams + security audit notes for all M2 programs"
```

**W8 — WEDNESDAY 2026-06-25**

```
BOOTCAMP (2h):
[ ] Solana Foundation Bootcamp: Final Week material + complete any assignments
[ ] Take final assessment if available

LEARN (1h):
[ ] Preview M3: AMM mechanics
    Read: "How Uniswap V2 Works" (EVM version — you know this)
    URL: https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works
    NOTE: Next month = build Solana AMM. Think through account design now.
    Draw: what accounts does an AMM need on Solana?

COMMIT:
[ ] Commit: "docs: AMM design notes (Solana port of Uniswap V2 mental model)"
```

**W8 — THURSDAY 2026-06-26**

```
PERSONAL BRAND (3h):
[ ] Update GitHub Profile README:
    - Add Projects section: counter (link), voting (link), token_manager (link), staking (link)
    - Each with: 1-line description, tech stack badges, devnet link
[ ] Update LinkedIn:
    - Summary update: "Solidity developer expanding into Rust/Solana for high-performance protocol development"
    - Add skills: Rust, Anchor, Solana
    - Add projects section with links
[ ] Check Twitter: respond to anyone who engaged with your threads

COMMIT:
[ ] Commit: "docs: GitHub profile README updated with M1+M2 projects"
```

**W8 — FRIDAY 2026-06-27**

```
LEARN (2h):
[ ] Metaplex: Umi framework (new TypeScript SDK)
    URL: https://developers.metaplex.com/umi
[ ] Comparison: @solana/web3.js vs Umi vs Anchor client

PRACTICE (1h):
[ ] Add Umi-based client to token_manager
[ ] Create token + mint using Umi client

COMMIT:
[ ] Commit: "feat: token_manager Umi client integration"
```

**W8 — SATURDAY 2026-06-28**

```
M2 RETROSPECTIVE + BLOG (3h):
[ ] Write Dev.to: "Month 2 Complete — 3 Solana Programs Deployed, First OSS PR"
    Include:
    - Programs: token_manager, voting, staking (links + program IDs)
    - OSS PR status
    - Biggest lesson: PDA design patterns
    - Hardest bug: [describe real bug you hit]
[ ] Fill M2 KPI summary

DEEP LEARN (2h):
[ ] Start Encode Club Bootcamp Review (cohort ends July 17)
    Complete any pending assignments
```

**W8 — SUNDAY 2026-06-29**
```
[ ] W8 KPI
[ ] Publish retrospective
[ ] REST
```

**W8 — MONDAY 2026-06-30**
> *Last day of June — M2 checkpoint*

```
[ ] Verify M2 Deliverables:
    [ ] 3 Anchor programs deployed devnet
    [ ] All tests passing (total: 13+ tests across 3 programs)
    [ ] 1 OSS PR submitted
    [ ] Solana Foundation Bootcamp: in progress / complete
    [ ] Encode Club Bootcamp: in progress
    [ ] 3 blog posts published
    [ ] GitHub profile updated
[ ] Set M3 goal: Staking devnet → mainnet, AMM build starts

COMMIT:
[ ] Commit: "chore: M2 checkpoint — all deliverables verified"
```

---

### ▶ MONTH 3 (M3): SPL Tokens Advanced + Mainnet Deploy Prep
**Calendar:** 2026-07-01 → 2026-07-31  
**Key Milestone:** First devnet-grade programs → mainnet-ready quality

---

#### ◆ WEEK 9 (W9): 2026-07-01 → 2026-07-07
**Theme:** Advanced PDAs + Mainnet preparation

**W9 — MONDAY 2026-07-01**

```
LEARN (2h):
[ ] Read: Solana Programs Security Guide
    URL: https://github.com/slowmist/solana-smart-contract-security-best-practices
[ ] For each vulnerability: add Anchor mitigation note
[ ] Checklist for mainnet readiness:
    [ ] No integer overflow (use checked_add, checked_sub, checked_mul)
    [ ] Signer verification on all mutations
    [ ] Owner checks (constraint = account.owner == program_id)
    [ ] No unchecked arithmetic
    [ ] Deterministic instruction handling
    [ ] No uninitialized accounts
    [ ] Proper error codes for all failure paths

AUDIT (1h):
[ ] Apply checklist to staking_program
[ ] Fix any issues found

COMMIT:
[ ] Commit: "security: staking_program mainnet readiness audit pass 1"
```

**W9 — TUESDAY 2026-07-02**

```
LEARN (2h):
[ ] Read: Verifiable Builds on Solana
    URL: https://solana.com/docs/programs/deploying#verifiable-builds
[ ] Install: cargo install solana-verify
[ ] Understand: why verifiable builds matter (trust, audit, open source)

BUILD (1h):
[ ] Prepare staking_program for verifiable build:
    - anchor build --verifiable
    - Check Anchor.toml: [features] seeds = true

COMMIT:
[ ] Commit: "build: staking_program verifiable build config"
```

**W9 — WEDNESDAY 2026-07-03**

```
BUILD (3h): START AMM DESIGN
[ ] Create: projects/amm/DESIGN.md
    Architecture decisions to document:
    [ ] Account structure: Pool { token_a_mint, token_b_mint, token_a_vault, token_b_vault, lp_mint, fee_rate, invariant }
    [ ] Instructions: create_pool, add_liquidity, remove_liquidity, swap_exact_in, swap_exact_out
    [ ] Math: constant product x*y=k, fee deduction, slippage protection
    [ ] LP tokens: how to calculate LP minted on add_liquidity
    [ ] Price impact calculation

COMMIT:
[ ] Commit: "docs: AMM architecture design document"
```

**W9 — THURSDAY 2026-07-04**
> *US Independence Day — lightweight day*

```
LEARN (2h):
[ ] Watch: "How Orca works" — Orca protocol docs (Solana's main AMM)
    URL: https://docs.orca.so/
[ ] Compare your AMM design with Orca's approach
[ ] Adjust DESIGN.md based on learnings

COMMIT:
[ ] Commit: "docs: AMM design updated with Orca comparison notes"
```

**W9 — FRIDAY 2026-07-05**

```
BUILD (3h): AMM SCAFFOLD
[ ] anchor init amm_program
[ ] Define all accounts in lib.rs:
    [ ] Pool struct (all fields from DESIGN.md)
    [ ] LiquidityPosition { owner, pool, lp_amount } (PDA)
[ ] Define all instruction handlers (empty bodies, just signatures)
[ ] anchor build (should compile)

COMMIT:
[ ] Commit: "feat: amm_program scaffold with account definitions"
```

**W9 — SATURDAY 2026-07-06**

```
BUILD (4h): AMM — create_pool + add_liquidity
[ ] Implement create_pool:
    [ ] Initialize Pool account
    [ ] Create LP mint with program as authority (PDA)
    [ ] Initialize token vaults (ATAs owned by pool PDA)
[ ] Implement add_liquidity:
    [ ] If first liquidity: lp_amount = sqrt(amount_a * amount_b)
    [ ] If not first: lp_amount = min(amount_a/reserve_a, amount_b/reserve_b) * total_lp
    [ ] CPI: transfer token_a from user to vault_a
    [ ] CPI: transfer token_b from user to vault_b
    [ ] CPI: mint LP tokens to user
[ ] Write unit tests for add_liquidity

COMMIT:
[ ] Commit: "feat: AMM create_pool + add_liquidity with LP token minting"
```

**W9 — SUNDAY 2026-07-07**
```
[ ] W9 KPI
[ ] REST
```

---

#### ◆ WEEK 10 (W10): 2026-07-08 → 2026-07-14
**Theme:** AMM swap logic + mainnet deploy first program

**W10 — MONDAY 2026-07-08**

```
BUILD (3h): AMM — swap_exact_in
[ ] Implement swap_exact_in(amount_in: u64, min_amount_out: u64):
    [ ] Calculate amount_out with x*y=k formula:
        fee_amount = amount_in * fee_rate / 10000
        amount_in_with_fee = amount_in - fee_amount
        amount_out = reserve_out * amount_in_with_fee / (reserve_in + amount_in_with_fee)
    [ ] Slippage check: require!(amount_out >= min_amount_out, SlippageExceeded)
    [ ] CPI: transfer token_in from user to vault_in
    [ ] CPI: transfer token_out from vault_out to user (invoke_signed with PDA)
    [ ] Update Pool reserves
[ ] Tests: swap 100 token_a, verify token_b received within expected range

COMMIT:
[ ] Commit: "feat: AMM swap_exact_in with constant product formula + slippage"
```

**W10 — TUESDAY 2026-07-09**

```
BUILD (3h): AMM — remove_liquidity + complete tests
[ ] Implement remove_liquidity(lp_amount: u64, min_a: u64, min_b: u64):
    [ ] Calculate withdrawal amounts: proportional to LP share
    [ ] Slippage checks for both tokens
    [ ] CPI: burn LP tokens
    [ ] CPI: transfer token_a from vault to user (invoke_signed)
    [ ] CPI: transfer token_b from vault to user (invoke_signed)
[ ] Write comprehensive test suite:
    [ ] create_pool
    [ ] add_liquidity (first + subsequent)
    [ ] swap (multiple, verify k stays constant)
    [ ] remove_liquidity
    [ ] edge: swap with slippage exceeded → error
[ ] anchor test (all pass)

COMMIT:
[ ] Commit: "feat: AMM complete — remove_liquidity + full test suite"
```

**W10 — WEDNESDAY 2026-07-10**

```
SECURITY (2h):
[ ] AMM security audit (self-audit):
    [ ] Price manipulation attack vector analysis
    [ ] Flash loan attack consideration
    [ ] Integer overflow in invariant calculation
    [ ] Reentrancy via CPI (check account refresh pattern)
    [ ] Fee collection — is it rug-able?
[ ] Fix any issues found
[ ] Document findings in: amm_program/SECURITY.md

COMMIT:
[ ] Commit: "security: AMM self-audit report + fixes"
```

**W10 — THURSDAY 2026-07-11**

```
MAINNET DEPLOY (2h):
[ ] Choose first program for mainnet: counter_program (simplest, battle-tested)
[ ] Steps:
    [ ] Switch to mainnet: solana config set --url mainnet-beta
    [ ] Fund deploy wallet (need ~0.1 SOL for deploy)
    [ ] anchor build --verifiable
    [ ] anchor deploy --provider.cluster mainnet
    [ ] Record Program ID: ___________________
    [ ] Verify on Solscan: https://solscan.io/account/[PROGRAM_ID]
[ ] Twitter: "First mainnet deploy! Counter program is live on Solana mainnet.
    Program ID: [ID]
    Verified build. No rugs here. 🦀🚀 #Solana #buildinpublic"

COMMIT:
[ ] Commit: "deploy: counter_program live on Solana MAINNET"
```

**W10 — FRIDAY 2026-07-12**

```
BUILD (2h):
[ ] AMM: add price oracle integration (mock)
    - get_price() function that reads pool reserves
    - Implement simple TWAP (time-weighted average price) over last N slots
[ ] This adds realism to the project — interviewers love TWAP

BOOTCAMP (1h):
[ ] Encode Club Bootcamp: final sessions, project submission (if any)

COMMIT:
[ ] Commit: "feat: AMM + simple TWAP oracle based on pool reserves"
```

**W10 — SATURDAY 2026-07-13**

```
BLOG (2h):
[ ] Write Dev.to: "Building a Constant Product AMM on Solana — Deep Dive"
    Sections:
    - The x*y=k formula (with worked examples)
    - LP token math (first deposit vs subsequent)
    - Why invoke_signed is needed for vault withdrawals
    - Security considerations
    - Code snippets + GitHub link + Devnet deploy

DEEP LEARN (2h):
[ ] Read: "From EVM to SVM" guide
    URL: https://www.zealynx.io/blogs/evm-to-svm-guide
[ ] Add 5 new insights to LEARNING_LOG
```

**W10 — SUNDAY 2026-07-14**
```
[ ] W10 KPI
[ ] Publish AMM blog
[ ] REST
```

---

#### ◆ WEEK 11 (W11): 2026-07-15 → 2026-07-21
**Theme:** Frontend integration + full-stack dApp polish

**W11 — MONDAY 2026-07-15**

```
BUILD (3h): NEXT.JS FRONTEND FOR AMM
[ ] npx create-next-app amm-frontend --typescript --tailwind --app
[ ] Install: @solana/web3.js, @coral-xyz/anchor, @solana/wallet-adapter-react
[ ] Setup wallet adapter (Phantom, Solflare)
[ ] Pages:
    [ ] / — Pool stats (reserves, TVL, fee rate)
    [ ] /swap — Token swap UI
    [ ] /pool — Add/remove liquidity UI

COMMIT:
[ ] Commit: "feat: AMM frontend Next.js scaffold with wallet adapter"
```

**W11 — TUESDAY 2026-07-16**

```
BUILD (3h): FRONTEND — Swap UI
[ ] Implement swap page:
    [ ] Token selector (dropdown)
    [ ] Input amount → calculate output preview (real-time)
    [ ] Slippage tolerance setting
    [ ] "Swap" button → triggers anchor transaction
    [ ] Success/error toast notifications
[ ] Connect to deployed devnet AMM program

COMMIT:
[ ] Commit: "feat: AMM swap UI with real-time quote calculation"
```

**W11 — WEDNESDAY 2026-07-17**

```
BUILD (2h): FRONTEND — Pool UI
[ ] Implement add/remove liquidity page
[ ] Real-time pool stats dashboard:
    [ ] Reserve A, Reserve B (formatted)
    [ ] Total LP supply
    [ ] 24h volume (mock for now)
    [ ] Current price A/B, B/A

COMMIT:
[ ] Commit: "feat: AMM liquidity UI + pool stats dashboard"
```

**W11 — THURSDAY 2026-07-18**

```
POLISH (2h):
[ ] Add error handling to all frontend transactions
[ ] Add loading states (skeleton screens)
[ ] Test with Phantom on devnet:
    [ ] Full flow: connect wallet → add liquidity → swap → remove liquidity
    [ ] Screenshot each step for blog/portfolio

COMMIT:
[ ] Commit: "polish: AMM frontend error handling + loading states + UX"
```

**W11 — FRIDAY 2026-07-19**

```
DEPLOY FRONTEND (1h):
[ ] Deploy to Vercel: vercel deploy
[ ] Custom domain if available: amm.lehongvo.dev (optional)
[ ] Add live URL to README

LEARN (2h):
[ ] Read: The Graph — Subgraph for Solana (via Bitquery alternative)
    URL: https://docs.bitquery.io/docs/schema/solana/
[ ] Alternative: Helius webhooks for real-time indexing
    URL: https://docs.helius.dev/webhooks-and-websockets/what-are-webhooks

COMMIT:
[ ] Commit: "deploy: AMM frontend live on Vercel"
[ ] Tweet link to live AMM demo
```

**W11 — SATURDAY 2026-07-20**

```
M3 BUFFER DAY (3h):
[ ] No new features. Review and polish only.
[ ] Review ALL 4 projects: counter, token_manager, voting, staking, AMM
[ ] Update karpathy-rust main README:
    | Project | Program Type | Devnet | Mainnet | Frontend | Tests |
    |---------|-------------|--------|---------|----------|-------|
    | Counter | Basic | ✅ | ✅ | — | 6/6 |
    | Token Mgr | SPL | ✅ | — | — | 3/3 |
    | Voting | Governance | ✅ | — | — | 4/4 |
    | Staking | DeFi | ✅ | — | — | 5/5 |
    | AMM | DeFi | ✅ | — | ✅ | 8/8 |
[ ] Prepare for Q1 Decision Gate (see Section 8)

BLOG:
[ ] Write Dev.to: "M3 Wrap: I Built a Full-Stack AMM on Solana"
    The journey from Counter → Token → Staking → AMM
```

**W11 — SUNDAY 2026-07-21**
```
[ ] W11 KPI
[ ] Publish blog
[ ] REST
```

---

#### ◆ WEEK 12 (W12): 2026-07-22 → 2026-07-31
**Theme:** Q1 Gate + Phase 2 Preparation + OSS Contribution #2

**W12 — MONDAY 2026-07-22**

```
DECISION GATE Q1 (1h):
See Section 8 for full Q1 Gate checklist.
[ ] Run Q1 Gate evaluation
[ ] Record result: GO / SLOW / NO-GO
[ ] If SLOW: identify specific gaps, create catch-up plan
[ ] If GO: write "Q1 GO — proceeding to Phase 2" in LEARNING_LOG

PLAN PHASE 2 (1h):
[ ] Review Phase 2 goals (Section 4)
[ ] Identify: which project for mainnet deploy in P2?
[ ] Research target companies list: start 30-company target list
    Columns: Company | Stack | Open Roles | Notes | Contact
```

**W12 — TUESDAY 2026-07-23**

```
LEARN (3h):
[ ] Read: Uniswap V2 Whitepaper (EVM)
    URL: https://uniswap.org/whitepaper.pdf
[ ] NOTE: You already know this (EVM background). Focus on:
    - Fee distribution mechanism
    - Flash swap mechanism
    - Price oracle (last block price)
[ ] Read: How Raydium differs from Orca (Solana AMMs)
    URL: https://docs.raydium.io/raydium/protocol/developers
[ ] NOTE differences in Solana account model vs your AMM design
```

**W12 — WEDNESDAY 2026-07-24**

```
OSS CONTRIBUTION #2 (3h):
[ ] Browse: Solana Cookbook GitHub
    URL: https://github.com/solana-developers/solana-cookbook/issues
[ ] Add example: "Building a minimal AMM with Anchor" (your working code!)
    - This is a real contribution — cookbook doesn't have this
[ ] Submit PR with:
    - Working code example
    - TypeScript test
    - Explanation prose
```

**W12 — THURSDAY 2026-07-25**

```
PERSONAL BRAND + NETWORKING (3h):
[ ] Twitter: post AMM architecture thread (with diagrams)
    Thread: "I built a Constant Product AMM on Solana. Here's every technical decision I made. 🧵"
    Include: account design, LP token math, TWAP oracle, security
[ ] Follow 20 Solana developers on Twitter (from hiring team lists):
    - Anchor framework contributors
    - Solana Foundation DevRel
    - Protocol engineers at Orca, Raydium, Kamino
[ ] LinkedIn: post about AMM project with GitHub link
[ ] Join Discord servers: Anchor Official, Solana Tech, Orca Protocol

COMMIT:
[ ] Commit: "docs: networking log — contacts made, servers joined"
```

**W12 — FRIDAY 2026-07-26**

```
RESEARCH (2h):
[ ] Research Phase 2 target companies (build list of 30):
    Start with:
    [ ] Drift Protocol (Solana perps)
    [ ] Kamino Finance (Solana lending)
    [ ] Zeta Markets (Solana options)
    [ ] Meteora (Solana liquidity)
    [ ] Marinade Finance (Solana staking)
    [ ] 1010 Trading (Rust + EVM)
    [ ] Caldera (Rust + EVM)
    [ ] Sei Foundation (Rust + EVM)
    [ ] Hyperliquid (Rust DEX)
    [ ] Mayan Finance (cross-chain)
    [ ] [Add 20 more from web3.career search]
[ ] For each: check open roles, tech stack, save to spreadsheet

COMMIT:
[ ] Commit: "docs: Phase 2 company target list v1 (30 companies)"
```

**W12 — SATURDAY 2026-07-27**

```
DEEP LEARN (4h):
[ ] Start reading: RareSkills "Zero Knowledge Proofs" free book
    URL: https://www.rareskills.io/zk-book
    Chapter 1-3 only (preview for Phase 3)
    NOTE: ZK is intimidating. Goal is just to understand "what a proof is" conceptually.
[ ] Read zk-learning.org introduction (1h)
    URL: https://zk-learning.org/
[ ] NOTE in LEARNING_LOG: "What I understand about ZK proofs after 2h reading"
```

**W12 — SUNDAY 2026-07-28**
```
[ ] W12 KPI
[ ] REST
```

**W12 — MONDAY 2026-07-29**

```
PHASE 1 FINAL REVIEW (3h):
[ ] Verify ALL Phase 1 deliverables (list below)
[ ] Create: PORTFOLIO.md in repo root
    Full portfolio document with:
    - Bio + contact
    - Skills matrix (Rust: intermediate, Solana/Anchor: intermediate, Solidity: strong)
    - Projects (name, description, program ID, test count, GitHub, live URL)
    - Blog posts (links)
    - OSS contributions (PR links)
    - Certificates (Solana Foundation Bootcamp if completed)
```

**W12 — TUESDAY 2026-07-30**

```
SOLANA FOUNDATION BOOTCAMP (3h):
[ ] If not yet: complete Solana Foundation Developer Bootcamp
    Complete all modules + final assessment
[ ] Download/save certificate
[ ] Add to LinkedIn Education section

TWITTER:
[ ] Post: "Phase 1 complete! 3 months of Rust + Solana.
    📊 Stats:
    - 5 Solana programs built
    - 1 mainnet deploy
    - 1 full-stack AMM dApp
    - ~26 blog posts / threads
    - 2 OSS PRs
    Phase 2 starts August 1: going production-grade. 🚀
    #Solana #Rust #Web3"
```

**W12 — WEDNESDAY 2026-07-31**
> *Last day of Phase 1*

```
FINAL COMMIT (1h):
[ ] Ensure all repos are clean and documented
[ ] Update all READMEs
[ ] Tag Phase 1 release: git tag v1.0-phase1-complete

[ ] Commit: "chore: Phase 1 complete — tagging v1.0-phase1-complete"
```

---

## ◉ PHASE 1 FINAL DELIVERABLES CHECKLIST

```
RUST FUNDAMENTALS:
[ ] Rustlings: 100% complete (all exercises)
[ ] Rust Book Ch 1–13: read and applied
[ ] Ownership/borrowing: can explain to a 5-year-old
[ ] async/await with tokio: working code

SOLANA PROGRAMS (all on devnet):
[ ] counter_program (Anchor + PDA) — also MAINNET ✅
[ ] token_manager (SPL + Token-2022 + Metaplex)
[ ] voting_program (double-vote-proof via PDA)
[ ] staking_program (time-based rewards, events)
[ ] amm_program (constant product, swap, LP tokens, TWAP)

TESTING:
[ ] Total tests across all programs: 26+
[ ] All tests passing
[ ] Clippy clean on all programs

FRONTEND:
[ ] AMM frontend deployed on Vercel
[ ] Full swap + liquidity flow working

PERSONAL BRAND:
[ ] GitHub profile README: portfolio + projects
[ ] Dev.to: 6+ posts published
[ ] Twitter: 8+ posts/threads
[ ] LinkedIn: updated with Rust/Solana skills + projects

OSS:
[ ] 2 OSS PRs submitted (Anchor, Solana Cookbook)

CERTIFICATIONS:
[ ] Solana Foundation Developer Bootcamp: in progress / complete

RESEARCH:
[ ] 30-company target list created
[ ] Phase 2 plan confirmed

HEALTH:
[ ] Burnout check: pace sustainable?
[ ] Commit streak: 50/66 weekdays (76%+ acceptable)
```