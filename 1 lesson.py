def sum_fib(n):
    a = 1
    b = 0
    c = 0
    while a < n:
        c += a
        a, b = a + b, a
        1return c

print(sum_fib(20))