import collections

def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def bfs(r, c):
        q = collections.deque()
        visit.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if ((r) in range(rows) and 
                    (c) in range(cols) and
                    grid[r][c] == '1' and
                    (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r, c))

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and (i, j) not in visit:
                bfs(i, j)
                islands += 1
    return islands
                