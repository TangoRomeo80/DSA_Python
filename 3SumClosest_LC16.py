class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')
        for i in range(n):
            l, r = i+1, n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return target
        return closest