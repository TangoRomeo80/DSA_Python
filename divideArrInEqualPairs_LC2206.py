from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for v in d.values():
            if v % 2 == 1:
                return False
        return True
