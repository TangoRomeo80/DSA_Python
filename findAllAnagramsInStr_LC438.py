import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # if len(s) < len(p):
        #     return []
        # result = []
        # pCounter = collections.Counter(p)
        # sCounter = collections.Counter(s[:len(p)-1])
        # for i in range(len(p)-1, len(s)):
        #     sCounter[s[i]] += 1
        #     if sCounter == pCounter:
        #         result.append(i-len(p)+1)
            
        #     sCounter[s[i-len(p)+1]] -= 1
        #     if sCounter[s[i-len(p)+1]] == 0:
        #         del sCounter[s[i-len(p)+1]]
        # return result

        if len(p) > len(s):
            return []
        pCount, sCount = {}, {}

        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1
        
        result = [0] if pCount == sCount else []
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                result.append(l)
            
        return result


        