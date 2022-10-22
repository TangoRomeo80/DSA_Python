class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                curr = ''
                while stack[-1] != '[':
                    curr = stack.pop() + curr
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * curr)
            else:
                stack.append(c)
        
        return ''.join(stack)