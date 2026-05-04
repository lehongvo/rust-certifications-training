# Day 1 — Bài 3: Variables & Mutability

## Mục tiêu
Hiểu `let`, `mut`, `const`, `static`, và shadowing — nền tảng để đọc bất kỳ code Rust nào.

## `let` — immutable mặc định

```rust
let x = 5;
x = 6; // ❌ error[E0384]: cannot assign twice to immutable variable
```

Lý do triết lý: an toàn concurrency, dễ reason về code, compiler tối ưu mạnh hơn.

## `mut` — opt-in mutability

```rust
let mut x = 5;
x = 6; // ✅ OK
```

Quy tắc: chỉ thêm `mut` khi **thực sự cần** mutate. Clippy sẽ warn nếu `mut` thừa.

## `const` — hằng số biên dịch

```rust
const MAX_POINTS: u32 = 100_000;
const PI: f64 = 3.14159;
```

- Phải có **type annotation**.
- Giá trị phải là **constant expression** (đánh giá tại compile-time).
- Quy ước đặt tên `SCREAMING_SNAKE_CASE`.
- Có thể khai báo ở **mọi scope**, kể cả global.

## `static` — biến có địa chỉ bộ nhớ cố định

```rust
static GREETING: &str = "Hello";
static mut COUNTER: u32 = 0; // unsafe để mutate
```

Khác `const`:
- `const` được **inline** ở mỗi nơi sử dụng (không có địa chỉ duy nhất).
- `static` có **một địa chỉ memory** cho toàn chương trình.
- Mutate `static mut` là `unsafe` — tránh dùng, ưu tiên `Mutex`/`Atomic`.

## Shadowing — khai báo lại cùng tên

```rust
let x = 5;
let x = x + 1;       // x = 6 (binding mới, immutable)
let x = x * 2;       // x = 12

let spaces = "   ";
let spaces = spaces.len(); // ✅ đổi cả type: &str → usize
```

So với `mut`:
- Shadowing tạo **biến mới**, có thể đổi type.
- `mut` chỉ thay giá trị, **không đổi type**.

```rust
let mut spaces = "   ";
spaces = spaces.len(); // ❌ mismatched types
```

## Type inference vs annotation

```rust
let x = 5;          // i32 (mặc định cho integer)
let y = 5.0;        // f64 (mặc định cho float)
let z: u64 = 5;     // explicit
let w = 5u64;       // suffix literal
```

Khi compiler không suy luận được:

```rust
let parsed: u32 = "42".parse().expect("not a number");
// hoặc
let parsed = "42".parse::<u32>().expect("not a number");
```

## Destructuring

```rust
let (a, b, c) = (1, 2, 3);
let [x, y, z] = [10, 20, 30];
let Point { x, y } = Point { x: 1, y: 2 };
```

## Pattern thông dụng

```rust
let _ = some_fn();           // bỏ qua giá trị trả về
let _unused = compute();     // giữ tên, im warning
let (mut a, b) = (1, 2);     // chỉ a là mutable
```

## Ghi chú
- Mặc định **immutable** giúp đọc code: thấy biến → biết không đổi.
- Shadowing dùng cho **transformation pipeline** (parse, normalize) là idiomatic.
- `const` cho config compile-time; `static` cho data có lifetime `'static` cần địa chỉ ổn định.
