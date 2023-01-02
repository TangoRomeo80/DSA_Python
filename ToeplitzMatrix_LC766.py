class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # compare the element with the element in the same column of the previous row
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True