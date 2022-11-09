from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]]
            #can't use both curEarn and earn2
            if i > 0 and nums[i] == nums[i - 1] + 1:
                earn1, earn2 = earn2, max(earn1 + curEarn, earn2)
            #use both curEarn and earn2
            else:
                earn1, earn2 = earn2, earn2 + curEarn
        return earn2
