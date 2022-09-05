def tribonacci(n):
    zero, one, two = 0, 1, 1

    for i in range(n):
        zero, one, two = one, two, zero + one + two

    return zero