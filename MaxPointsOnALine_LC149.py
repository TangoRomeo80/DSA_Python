class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        res = 0
        for i in range(len(points)):
            d = {}
            same = 1
            for j in range(i+1, len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same += 1
                elif points[i][0] == points[j][0]:
                    d['inf'] = d.get('inf', 0) + 1
                else:
                    k = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    d[k] = d.get(k, 0) + 1
            res = max(res, same + max(d.values()) if d else same)
        return res