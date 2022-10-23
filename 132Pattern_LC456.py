class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] #pair [num, min] mono decreasing
        curMin = nums[0]

        for n in nums[1:]:
            if n < curMin:
                curMin = n
            elif n > curMin:
                while stack and stack[-1][0] <= n:
                    stack.pop()
                if stack and stack[-1][1] < n:
                    return True
                stack.append([n, curMin])
                
        return False

