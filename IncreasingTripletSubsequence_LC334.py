class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min1 = nums[0]
        min2 = float('inf')
        for i in range(1, len(nums)):
            if nums[i] > min2:
                return True
            if nums[i] > min1:
                min2 = nums[i]
            else:
                min1 = nums[i]
        return False