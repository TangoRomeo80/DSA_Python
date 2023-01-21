class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True

        for i in range(3):
            mat = self.rotate(mat)
            if mat == target:
                return True

        return False

    def rotate(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        for i in range(n):
            mat[i].reverse()

        return mat
        