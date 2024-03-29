class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # # O(n^2) time, O(1) space
        # for i in range(1, len(s)):
        #     if len(s) % i == 0:
        #         if s[:i] * (len(s) // i) == s:
        #             return True
        # return False

        n, t = len(s), ''
        for i in range(n // 2):
            t += s[i]
            if t* (n // (i+1)) == s: 
                return True
        return False

