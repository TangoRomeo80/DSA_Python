def arrangeCoins(n):
    # count = 0
    # while n > 0:
    #     n -= count + 1
    #     if n > 0:
    #         count += 1
    # return count

    l, r = 1, n
    res = 0

    while l <= r:
        mid = (l + r) // 2
        if mid * (mid + 1) // 2 <= n:
            res = max(mid, res)
            l = mid + 1
        else:
            r = mid - 1
    return res


print(arrangeCoins(5))