class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        col = [0] * n
        for i in indices:
            row[i[0]] += 1
            col[i[1]] += 1
        count = 0
        for i in range(m):
            for j in range(n):
                if (row[i] + col[j]) % 2 != 0:
                    count += 1
        return count