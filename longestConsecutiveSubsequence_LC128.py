class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # nums = set(nums)
        # maxLen = 0
        # for num in nums:
        #     if num - 1 not in nums:
        #         currNum = num
        #         currLen = 1
        #         while currNum + 1 in nums:
        #             currNum += 1
        #             currLen += 1
        #         maxLen = max(maxLen, currLen)
        # return maxLen
        
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest