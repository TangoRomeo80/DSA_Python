class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # count the number of 0 and 1
        # if the number of 0 and 1 are the same, then we can add the number of 0 and 1
        # if the number of 0 and 1 are not the same, then we can add the minimum number of 0 and 1
        count = 0
        prev = 0
        curr = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                count += min(prev, curr)
                prev = curr
                curr = 1
        count += min(prev, curr)
        return count