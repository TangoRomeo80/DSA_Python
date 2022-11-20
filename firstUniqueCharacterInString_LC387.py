from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        #Time: O(n)
        #Space: O(n)
        
        d = Counter(s)
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
