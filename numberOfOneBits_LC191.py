def hammingWeight(n):

    # return bin(n).count('1')
    res = 0
    while n:
        n &= n - 1
        res += 1
    return res

print(hammingWeight(7))