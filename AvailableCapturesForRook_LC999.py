class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find the rook
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook = (i, j)
                    break
        # check the 4 directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        for d in directions:
            x, y = rook[0] + d[0], rook[1] + d[1]
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p':
                    res += 1
                    break
                if board[x][y] == 'B':
                    break
                x += d[0]
                y += d[1]

        return res
