class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binSearch(nums, target, True), self.binSearch(nums, target, False)]

    #leftBias = if false res is rightmost index
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = l + (r - l) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i
        
        
