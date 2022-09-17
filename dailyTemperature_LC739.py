class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #O(n^2) solution
        # res = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        # return res

        #O(n) solution
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res