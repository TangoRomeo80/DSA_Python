class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDist = float('inf')
        minIndex = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                dist = abs(points[i][0] - x) + abs(points[i][1] - y)
                if dist < minDist:
                    minDist = dist
                    minIndex = i
        return minIndex