class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            sub = nums[l[i]:r[i]+1]
            sub.sort()
            diff = sub[1] - sub[0]
            flag = True
            for j in range(2, len(sub)):
                if sub[j] - sub[j-1] != diff:
                    flag = False
                    break
            res.append(flag)
        return res