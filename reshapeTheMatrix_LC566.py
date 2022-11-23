class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        else:
            flat = []
            newMat = []
            for row in mat:
                for num in row:
                    flat.append(num)
            for i in range(r):
                newMat.append(flat[i*c:(i+1)*c])
            return newMat