class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1. use hash table to store the count of each number
        # 2. loop through the hash table and find the number with count 1
        # 3. return the number
        # time O(n) space O(n)
        # if not nums:
        #     return None
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        # for key, val in count.items():
        #     if val == 1:
        #         return key
        # return None

        # time O(n) space O(1)
        # Let the numbers be x,y,z,.....
		# require sum should be 3x+3y+3z
		# original sum = 3x+3y+z
		# Subtract require sum from original sum
		# (3x+3y+3z) - (3x+3y-z) = 2z
		# div the ans by 2 = 2z/2 = z--> our ans

	    return (3 * sum(set(nums)) - sum(nums)) // 2

        
        