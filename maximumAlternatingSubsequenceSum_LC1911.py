class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        #Recursive solution
        #Time: O(n)
        #Space: O(n)

        # dp = {} # key: (index, even/odd), value: max alternating sum

        # def dfs(i, even):
        #     if i == len(nums):
        #         return 0
        #     if (i, even) in dp:
        #         return dp[(i, even)]
            
        #     total = nums[i] if even else (- 1 * nums[i])
        #     dp[(i, even)] = max(total + dfs(i + 1, not even), dfs(i + 1, even))
        #     return dp[(i, even)]
        
        # return dfs(0, True)

        #Iterative solution
        #Time: O(n)
        #Space: O(1)

        sumEven, sumOdd = 0, 0

        for i in range(len(nums) - 1, -1 , -1):
            tmpEven = max(sumOdd + nums[i], sumEven)
            tmpOdd = max(sumEven - nums[i], sumOdd)
            sumEven, sumOdd = tmpEven, tmpOdd

        return sumEven
        