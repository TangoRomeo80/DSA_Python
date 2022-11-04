class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = {s for s in nums}

        def backtrack(i, cur):
            if i == len(nums):
                res = ''.join(cur)
                return None if res in strSet else res
            
            res = backtrack(i + 1, cur)
            if res:
                return res
            cur[i] = '1' if cur[i] == '0' else '0'
            res = backtrack(i + 1, cur)
            if res:
                return res

        return backtrack(0, ['0' for s in nums])  
        
