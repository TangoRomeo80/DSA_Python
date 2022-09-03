def shiftGrid(grid, k):
    M, N = len(grid), len(grid[0])

    def posToVal(r, c):
        return (r * N) + c

    def valToPos(v):
        return (v // N, v % N)

    res = [[0] * N for i in range(M)]

    for r in range(M):
        for c in range(N):
            v = posToVal(r, c)
            v = (v + k) % (M * N)
            r1, c1 = valToPos(v)
            res[r1][c1] = grid[r][c]

    return res
