
def print_solution(board, n):
    print('\n'.join([' '.join([str(item) for item in row])for row in board]))


def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solver_func(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solver_func(board, col + 1, n):
                return True
            board[i][col] = 0

    return False


def solve(n):
    board = [[0 for x in range(n)] for y in range(n)]
    if not solver_func(board, 0, n):
        print("Solution does not exist")
        return False

    print_solution(board, n)
    return True


N = int(input('Enter N value: '))
solve(N)

