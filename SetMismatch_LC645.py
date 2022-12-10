class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 1. Find the sum of the array
        sum_of_array = sum(nums)
        
        # 2. Find the sum of the set
        sum_of_set = sum(set(nums))
        
        # 3. Find the duplicate number
        duplicate = sum_of_array - sum_of_set
        
        # 4. Find the missing number
        missing = int((n*(n+1)/2) - sum_of_set)
        
        return [duplicate, missing]