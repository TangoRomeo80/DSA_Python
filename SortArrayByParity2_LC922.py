class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # # Time: O(N)
        # # Space: O(N)
        # even = []
        # odd = []
        # for num in nums:
        #     if num % 2 == 0:
        #         even.append(num)
        #     else:
        #         odd.append(num)
        # res = []
        # for i in range(len(even)):
        #     res.append(even[i])
        #     res.append(odd[i])
        # return res

        # Time: O(N)
        # Space: O(1)
        i, j, L = 0, 1, len(nums)             
        while j < L:                          
            if nums[j] % 2 == 0:              
                nums[j], nums[i] = nums[i], nums[j]     
                i += 2                         
            else:
                j += 2                         
        return nums