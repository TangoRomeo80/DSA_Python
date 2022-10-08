class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Time: O(n)
        # Space: O(n)
        # n = len(wall)
        # 1. Create a map of current total position to number of bricks
        # 2. Find the total that has the most bricks
        # 3. Return n - maxEdge
        countGap = {}
        for row in wall:
            total = 0
            for brick in row[:-1]:
                total += brick
                countGap[total] = countGap.get(total, 0) + 1
        if countGap:
            return len(wall) - max(countGap.values())
        else:
            return len(wall)