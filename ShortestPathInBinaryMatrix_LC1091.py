from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1:
            return 1
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1
        while queue:
            x, y = queue.popleft()
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return grid[x][y]
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))
        return -1