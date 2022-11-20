from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        d = Counter(nums1)
        res = []
        for num in nums2:
            if num in d and d[num] != 0:
                res.append(num)
                d[num] -= 1
        return res

solution = Solution()
print(solution.intersect([4,9,5], [9,4,9,8,4]))