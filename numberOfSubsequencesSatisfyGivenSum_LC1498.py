class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        #gets TLE
        # nums.sort()
        # res = 0
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     if nums[l] + nums[r] > target:
        #         r -= 1
        #     else:
        #         res += 2 ** (r - l)
        #         l += 1
        # return res % (10 ** 9 + 7)

        #TLE as well
        # nums.sort()
        # res = 0
        # r = len(nums) - 1
        # for i in range(len(nums)):
        #     while (nums[i] + nums[r]) > target and i <= r:
        #         r -= 1
        #     if i <= r:
        #         res += 2 ** (r - i)
        #         res %= (10 ** 9 + 7)  
        # return res % (10 ** 9 + 7) 

        #AC
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod   
            
        