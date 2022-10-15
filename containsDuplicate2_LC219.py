class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = {}
        for i, n in enumerate(nums):
            if n in c and abs(c[n] - i) <= k:
                return True
            else:
                c[n] = i
        return False