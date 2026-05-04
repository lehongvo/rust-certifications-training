# Day 1 — Bài 2: Hello Cargo

## Mục tiêu
Làm chủ `cargo` — công cụ build/run/test/dependency mặc định của Rust.

## Tạo project

```bash
cargo new hello_cargo          # binary project (mặc định)
cargo new mylib --lib          # library project
cargo init                     # khởi tạo trong thư mục hiện tại
```

Cấu trúc sinh ra:

```
hello_cargo/
├── Cargo.toml      # manifest: metadata + dependencies
├── .gitignore
└── src/
    └── main.rs     # entry point của binary
```

## `Cargo.toml` cơ bản

```toml
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"     # edition: 2015 / 2018 / 2021 / 2024

[dependencies]
# tên_crate = "version"
```

`Cargo.lock` sinh tự động — pin chính xác version, **commit** với binary, **gitignore** với library.

## Lệnh thường dùng

| Lệnh | Tác dụng |
|---|---|
| `cargo build` | Build debug → `target/debug/<name>` |
| `cargo build --release` | Build optimize → `target/release/<name>` |
| `cargo run` | Build + chạy binary |
| `cargo run -- arg1 arg2` | Truyền args sau `--` |
| `cargo check` | Type-check không sinh binary (nhanh hơn build) |
| `cargo test` | Chạy unit + integration tests |
| `cargo fmt` | Format code |
| `cargo clippy` | Lint |
| `cargo doc --open` | Sinh docs cho deps + project, mở trình duyệt |
| `cargo clean` | Xoá `target/` |

## Hello World

`src/main.rs`:

```rust
fn main() {
    println!("Hello, cargo!");
}
```

```bash
cargo run
# Compiling hello_cargo v0.1.0 ...
# Finished `dev` profile ...
# Running `target/debug/hello_cargo`
# Hello, cargo!
```

## `println!` — nó là **macro**, không phải hàm

Dấu `!` đánh dấu macro:

```rust
println!("x = {}", 42);            // positional
println!("x = {x}", x = 42);       // named
println!("x = {x}");               // capture variable trong scope
println!("{:?}", vec![1, 2, 3]);   // Debug format → [1, 2, 3]
println!("{:#?}", vec![1, 2, 3]);  // pretty Debug
```

## Workspace (multi-package)

`Cargo.toml` ở root:

```toml
[workspace]
members = ["pkg_a", "pkg_b"]
resolver = "2"
```

Cho phép share `target/` và `Cargo.lock` giữa nhiều crate.

## Ghi chú
- `cargo check` là bạn thân — chạy liên tục khi code, nhanh gấp 3-5 lần `build`.
- `target/` luôn nằm trong `.gitignore`.
- Đặt `RUST_BACKTRACE=1` để hiện stack trace khi panic.
