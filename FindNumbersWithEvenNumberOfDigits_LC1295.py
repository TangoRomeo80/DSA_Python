class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # count = 0
        # for num in nums:
        #     if len(str(num)) % 2 == 0:
        #         count += 1
        # return count

        result = 0
        
        for num in nums:
            num_digits = floor(log10(num)) + 1
            if num_digits % 2 == 0:
                result += 1
                
        return result