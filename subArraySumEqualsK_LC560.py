class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # O(n^2) solution
        # count = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             count += 1
        # return count

        # O(n) solution
        count = 0
        sum = 0
        sumDict = {0:1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in sumDict:
                count += sumDict[sum - k]
            sumDict[sum] = sumDict.get(sum, 0) + 1
        return count