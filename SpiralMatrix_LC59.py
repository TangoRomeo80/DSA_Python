class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        res = [[0 for i in range(n)] for j in range(n)]
        l, r, t, b, n = 0, n - 1, 0, n - 1, 1
        while l <= r and t <= b:
            for i in range(l, r + 1):
                res[t][i] = n
                n += 1
            t += 1
            for i in range(t, b + 1):
                res[i][r] = n
                n += 1
            r -= 1
            for i in range(r, l - 1, -1):
                res[b][i] = n
                n += 1
            b -= 1
            for i in range(b, t - 1, -1):
                res[i][l] = n
                n += 1
            l += 1

        return res