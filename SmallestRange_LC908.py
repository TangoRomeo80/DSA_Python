class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        if max_num - min_num <= 2 * k:
            return 0
        return max_num - min_num - 2 * k