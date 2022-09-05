def fib(n):
    zero, one = 0, 1

    for i in range(n):
        zero, one = one, zero + one

    return zero