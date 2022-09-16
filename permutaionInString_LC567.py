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
        # c1 = Counter(s1)

        # for i in range(len(s2)-len(s1)+1):
        #     if c1 == Counter(s2[i:i+len(s1)]):
        #         return True
        # return False

        #O(n)
        


        
                    
            

        
        
x = Solution()
x.checkInclusion("ab", "eidbaooo")
