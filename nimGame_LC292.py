class Solution:
    def canWinNim(self, n: int) -> bool:
        #one-liner
        #return n%4 != 0

        #brute force(gets TLE)
        # if n <= 3:
        #     return True
        # return not (self.canWinNim(n-1) and self.canWinNim(n-2) and self.canWinNim(n-3))

        #DP
        dp = [True, True, True, False]
        if n <= 3:
            return dp[n - 1]
        for i in range(4, n+1):
            dp.append(not (dp[i-1] and dp[i-2] and dp[i-3]))    
        return dp[n - 1]

