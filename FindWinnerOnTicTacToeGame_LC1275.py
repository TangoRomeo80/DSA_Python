class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        anti_diag = 0
        player = 1
        for x, y in moves:
            rows[x] += player
            cols[y] += player
            if x == y:
                diag += player
            if x + y == 2:
                anti_diag += player
            if any(abs(line) == 3 for line in (rows[x], cols[y], diag, anti_diag)):
                return "A" if player == 1 else "B"
            player *= -1
        return "Draw" if len(moves) == 9 else "Pending"