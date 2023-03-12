class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        num = 0
        for i in range(len(nums)):
            num = num * 2 + nums[i]
            res.append(num % 5 == 0)
        return res