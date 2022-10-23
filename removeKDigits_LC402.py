class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)

        while k > 0:
            stack.pop()
            k -= 1
        
        res = ''.join(stack)
        return str(int(res)) if res else '0'