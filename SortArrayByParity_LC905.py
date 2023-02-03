class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # O(n) time, O(n) space
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd

        # O(n) time, O(1) space
        # i = 0
        # j = len(nums) - 1
        # while i < j:
        #     if nums[i] % 2 == 0:
        #         i += 1
        #     elif nums[j] % 2 == 1:
        #         j -= 1
        #     else:
        #         nums[i], nums[j] = nums[j], nums[i]
        # return nums