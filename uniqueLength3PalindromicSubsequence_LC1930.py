import collections

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        for c in set(s):
            i, j = s.find(c), s.rfind(c)
            count += len(set(s[i+1:j]))
        return count

        # res = set()
        # left = set()
        # right = collections.Counter(s)

        # for i in range(len(s)):
        #     right[s[i]] -= 1
        #     if right[s[i]] == 0:
        #         right.pop(s[i])
            
        #     for j in range(26):
        #         c = chr(ord('a') + j)
        #         if c in left and c in right:
        #             res.add((s[i], c))
            
        #     left.add(s[i])
    
        # return len(res)

