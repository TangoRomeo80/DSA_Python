class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if not s:
            return 0
        count = 0
        r_count = 0
        l_count = 0
        for i in range(len(s)):
            if s[i] == 'R':
                r_count += 1
            else:
                l_count += 1
            if r_count == l_count:
                count += 1
                r_count = 0
                l_count = 0
        return count