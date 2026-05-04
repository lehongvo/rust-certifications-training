# Day 1 — Bài 1: Setup Toolchain

## Mục tiêu
Cài đặt môi trường Rust và hiểu vai trò của từng thành phần trong toolchain.

## Toolchain cốt lõi

| Thành phần | Vai trò |
|---|---|
| `rustup` | Quản lý phiên bản Rust (stable/beta/nightly), thêm target & component |
| `rustc` | Trình biên dịch Rust |
| `cargo` | Build system + package manager (giống `npm`/`go mod` của Rust) |
| `rustfmt` | Tự động format code |
| `clippy` | Linter, gợi ý best practice |

## Cài đặt (macOS / Linux)

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

Kiểm tra:

```bash
rustc --version      # rustc 1.xx.x
cargo --version
rustup --version
```

## Toolchain channels

- **stable** — phát hành mỗi 6 tuần, dùng cho production.
- **beta** — preview của stable kế tiếp.
- **nightly** — cập nhật mỗi đêm, có feature thử nghiệm (`#![feature(...)]`).

```bash
rustup show                        # toolchain hiện tại
rustup toolchain install nightly   # thêm nightly
rustup default stable              # mặc định stable
rustup update                      # nâng cấp tất cả
```

## Components hữu ích

```bash
rustup component add rustfmt
rustup component add clippy
rustup component add rust-src        # source std (cho rust-analyzer)
rustup component add rust-analyzer   # LSP server
```

## IDE setup

- **VS Code**: extension `rust-analyzer` (chính thức, KHÔNG dùng `Rust` cũ).
- **JetBrains**: RustRover hoặc plugin Rust cho IntelliJ/CLion.
- **Vim/Neovim**: `rust-analyzer` qua LSP.

## Verify nhanh

```bash
cargo new hello && cd hello && cargo run
```

Nếu in ra `Hello, world!` → toolchain OK.

## Ghi chú
- Cài `rustup` thay vì `brew install rust` để dễ quản lý nhiều version.
- Source `~/.cargo/env` trong `.zshrc`/`.bashrc` để `cargo` luôn có trong PATH.
