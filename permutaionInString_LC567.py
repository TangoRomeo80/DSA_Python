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
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
 
        
x = Solution()
x.checkInclusion("ab", "eidbaooo")
