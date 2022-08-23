def searchInsert(self, nums, target):
    #O(n)
        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         return i
        # return len(nums)
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return l