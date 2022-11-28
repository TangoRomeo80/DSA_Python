class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 1. linear scan
        # 2. count the consecutive 1s
        # 3. update the max
        # 4. return the max
        maxCount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        maxCount = max(maxCount, count)
        return maxCount