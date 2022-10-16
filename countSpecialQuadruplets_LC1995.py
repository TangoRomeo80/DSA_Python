from collections import defaultdict

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        #O(n^4)
        # count, n = 0, len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             for l in range(k+1,n):
        #                 if (nums[i] + nums[j] + nums[k]) == nums[l]:
        #                     count += 1
        # return count

        #O(n^3)
        # seenAlready = {}
        # n = len(nums)
        # count = 0
        # for a in range(n-1,-1,-1):
        #     for b in range(a-1,-1,-1):
        #         for c in range(b-1,-1,-1):
        #             possibleSum = nums[a]+nums[b]+nums[c]
        #             if possibleSum in seenAlready:
        #                 count += seenAlready[possibleSum]
        #     seenAlready[nums[a]] = seenAlready.get(nums[a], 0) + 1
        # return count

        #O(n^2)
        count = 0
        n = len(nums)
        seenAlready = defaultdict(int)
        for a in range(n-1,0,-1):
            for b in range(a-1,-1,-1):
                count += seenAlready[nums[a]+nums[b]]
            for d in range(n-1,a,-1):
                seenAlready[nums[d]-nums[a]] += 1
        return count