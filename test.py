from cffi import FFI

def init():
    ffi = FFI()
    lib = ffi.dlopen("./liblibcoba.dylib")
    ffi.cdef('int sum_n_fibonacci(int);')
    sum_n_fibonacci(10)
    # sum_n_fibonacci_rust(lib,10)

def sum_n_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sum_n_fibonacci(n-2) + sum_n_fibonacci(n-1)

def sum_n_fibonacci_rust(lib,n):
    lib.sum_n_fibonacci(n)
