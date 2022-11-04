class Solution:
    def romanToInt(self, s: str) -> int:
        rti = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0

        for i in range(len(s)):
            if i > 0 and rti[s[i]] > rti[s[i-1]]:
                res += rti[s[i]] - 2*rti[s[i-1]]
            else:
                res += rti[s[i]]
        
        return res
        
