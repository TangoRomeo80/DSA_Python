class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #bucket sort
        bucket = [0,0,0]
        for i in nums:
            bucket[i] += 1
        i = 0
        for j in range(3):
            while bucket[j] > 0:
                nums[i] = j
                i += 1
                bucket[j] -= 1
        
