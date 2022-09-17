class Solution:
    #solution using decision tree
    # def dfs(self, left, right, s, res):
    #     if left == 0 and right == 0:
    #         res.append(s)
    #         return
    #     if left > 0:
    #         self.dfs(left-1, right, s+'(', res)
    #     if right > left:
    #         self.dfs(left, right-1, s+')', res)

    def generateParenthesis(self, n: int) -> List[str]:
        # if n == 0:
        #     return []
        # if n == 1:
        #     return ["()"]
        # res = []
        # self.dfs(n, n, "", res)
        # return res

        #solution using stack
        # if n == 0:
        #     return []
        # if n == 1:
        #     return ["()"]
        # res = []
        # stack = [(n, n, "")]
        # while stack:
        #     left, right, s = stack.pop()
        #     if left == 0 and right == 0:
        #         res.append(s)
        #     if left > 0:
        #         stack.append((left-1, right, s+'('))
        #     if right > left:
        #         stack.append((left, right-1, s+')'))
        # return res

        #solution using backtracking
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res