def missingNumber(nums):
    # hash map solution
#         d = {}
#         for i in range(len(nums)):
#             d[nums[i]] = True

#         for i in range(len(nums) + 1):
#             if i not in d:
#                 return i

        
        #sum solution
#         s = sum(nums)
#         t = sum(range(len(nums) + 1))
        
#         return t - s

        #sum solution optimized
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res
    
print(missingNumber([9,6,4,2,3,5,7,0,1]))