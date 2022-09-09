import math

def minEatingSpeed(piles, h):
    # binary search init
    l, r = 1, max(piles)

    k = 0

    while l <= r:
        m = (l + r) // 2

        totalTime = 0
        for p in piles:
            totalTime += math.ceil(p / m)

        if totalTime <= h:
            r = m - 1
            k = m
        else:
            l = m + 1
    
    return k

