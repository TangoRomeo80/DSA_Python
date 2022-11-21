from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = Counter(s)
        for c in t:
            d[c] -= 1
            if d[c] < 0:
                return c
        