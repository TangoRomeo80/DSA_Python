class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        #O(n^2)
        # res = []
        # for i in range(len(s)):
        #     if s[i] == c:
        #         res.append(0)
        #     else:
        #         res.append(min([abs(i-j) for j in range(len(s)) if s[j] == c]))

        # return res

        #O(n)
        res = []
        prev = float('-inf')
        for i in range(len(s)):
            if s[i] == c:
                prev = i
            res.append(i - prev)

        prev = float('inf')
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                prev = i
            res[i] = min(res[i], prev - i)

        return res
