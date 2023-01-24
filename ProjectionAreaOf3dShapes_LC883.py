class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # 1. top view
        top = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    top += 1
        # 2. front view
        front = 0
        for i in range(len(grid)):
            front += max(grid[i])
        # 3. side view
        side = 0
        for i in range(len(grid[0])):
            side += max([grid[j][i] for j in range(len(grid))])
        return top + front + side