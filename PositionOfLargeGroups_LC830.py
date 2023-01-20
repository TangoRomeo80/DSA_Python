class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) < 3:
            return []
        res = []
        start = 0
        for i in range(1, len(s)):
            if s[i] != s[start]:
                if i - start >= 3:
                    res.append([start, i - 1])
                start = i
        if len(s) - start >= 3:
            res.append([start, len(s) - 1])
        return res