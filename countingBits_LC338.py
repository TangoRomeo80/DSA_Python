def countBits(n):
    
        #Python built in function solution(Most efficient????)
        # res = []
        # for i in range(n+1):
        #     res.append(bin(i).count('1'))
        # return res
        
        #Bit manipulation solution
        # res = [0] * (n+1)
        # for i in range(1, n+1):
        #     res[i] = res[i >> 1] + (i & 1)
        # return res
        
        #DP solution
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
    