import heapq

def kClosest(points, k):
    # return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]
    pts = []
    for x, y in points:
        dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
        pts.append([dist, x, y])

    res = []
    heapq.heapify(pts)
    for i in range(k):
        dist, x, y = heapq.heappop(pts)
        res.append([x, y])
    return res