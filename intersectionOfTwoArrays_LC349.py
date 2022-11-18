from collections import Counter

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        
        # nums1 = set(nums1)
        # nums2 = set(nums2)
        
        # return list(nums1.intersection(nums2))

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        d = Counter(nums1)

        res = []
        for num in nums2:
            if num in d:
                res.append(num)
                del d[num]
        return res
        