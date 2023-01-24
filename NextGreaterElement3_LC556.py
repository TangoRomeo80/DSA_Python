class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10:
            return -1
        n = str(n)
        n = list(n)
        i = len(n) - 2
        while i >= 0 and n[i] >= n[i+1]:
            i -= 1
        if i < 0:
            return -1
        j = len(n) - 1
        while j > i and n[j] <= n[i]:
            j -= 1
        n[i], n[j] = n[j], n[i]
        n[i+1:] = n[i+1:][::-1]
        n = int(''.join(n))
        return n if n < 2**31 else -1