import collections

def isValidSudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    boxes = collections.defaultdict(set)

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in cols[j] or board[i][j] in rows[i] or board[i][j] in boxes[(i//3, j//3)]:
                    return False
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                boxes[(i//3, j//3)].add(board[i][j])

    return True