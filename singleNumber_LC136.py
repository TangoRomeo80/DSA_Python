def singleNumberHash(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in d:
        if d[i] == 1:
            return i


def singleNumberBit(nums):
    res = 0
    for n in nums:
        res ^= n
    return res