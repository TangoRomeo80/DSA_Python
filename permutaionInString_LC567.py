from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #O(n^2)
        # s1 = sorted(s1)
        # for i in range(len(s2)-len(s1)+1):
        #     if sorted(s2[i:i+len(s1)]) == s1:
        #         return True
        # return False

        #O(26.n)
        def isAnagram(s, t):
            if len(s) != len(t):
                return False
            d = {}
            for i in s:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            for i in t:
                if i in d:
                    d[i] -= 1
                else:
                    d[i] = 1
            for i in d:
                if d[i] != 0:
                    return False
            return True

        if len(s1) > len(s2):
            return False
        for i in range(len(s2)-len(s1)+1):
            if isAnagram(s1, s2[i:i+len(s1)]):
                return True
        return False
                    
            

        
        
x = Solution()
x.checkInclusion("ab", "eidbaooo")
