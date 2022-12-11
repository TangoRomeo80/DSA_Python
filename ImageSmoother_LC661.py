class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        res = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                count = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x >= 0 and x < m and y >= 0 and y < n:
                            res[i][j] += img[x][y]
                            count += 1
                res[i][j] = res[i][j] // count
        return res