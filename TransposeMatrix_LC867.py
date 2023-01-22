class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # return list(zip(*matrix))
        res = []
        for i in range(len(matrix[0])):
            res.append([row[i] for row in matrix])
        return res