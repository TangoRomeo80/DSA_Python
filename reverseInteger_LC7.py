def reverse(x):
    if x < 0:
        x = -x
        sign = -1
    else:
        sign = 1
    res = 0
    while x > 0:
        res = res * 10 + x % 10
        x = x // 10
    if(res > 2**31):
        return 0
    return res * sign

    