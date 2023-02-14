from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        c = Counter(nums)
        for k, v in c.items():
            if v == n:
                return k
            
    