#![crate_type = "dylib"]

#[no_mangle]
pub extern fn sum_n_fibonacci(n: i32) -> i32 {
    if n == 0 {
        0
    } else if n == 1 {
        1
    } else {
        sum_n_fibonacci(n-2) + sum_n_fibonacci(n-1)
    }
}
