class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # Time: O(N)
        # Space: O(N)
        n = len(s)
        res = [0] * (n + 1)
        lo, hi = 0, n
        for i in range(n):
            if s[i] == 'I':
                res[i] = lo
                lo += 1
            else:
                res[i] = hi
                hi -= 1
        res[n] = lo
        return res