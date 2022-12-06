from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # count the frequency of each number
        freq = Counter(nums)
        # find the longest harmonious subsequence
        longest = 0
        for num in freq:
            if num + 1 in freq:
                longest = max(longest, freq[num] + freq[num + 1])
        return longest