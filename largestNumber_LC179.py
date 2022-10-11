from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(a, b):
            return 1 if a + b > b + a else -1
        
        nums = sorted(nums, key=cmp_to_key(compare), reverse=True)
        
        return str(int(''.join(nums)))