class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
        # if len(s) == 0:
        #     return 0
        # count = 0
        # for i in range(len(s)):
        #     if i == 0 and s[i] != " ":
        #         count += 1
        #     elif i > 0 and s[i] != " " and s[i - 1] == " ":
        #         count += 1
        # return count
        