class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        numsCopy = []
        for i in range(len(nums)):
            numsCopy.append(nums[i])

        if len(nums) == 1:
            return 0
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        if max1 >= 2*max2:
            return numsCopy.index(max1)
        return -1