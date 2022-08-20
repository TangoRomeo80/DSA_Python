import heapq

def lastStoneWeight(self, stones):
    # while len(stones) > 1:
    #     stones.sort()
    #     x = stones.pop()
    #     y = stones.pop()
    #     if x != y:
    #         stones.append(x - y)
    # return stones[0] if stones else 0

    #maxheap implementation
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first:
            heapq.heappush(stones, first - second)

    stones.append(0)
    return abs(stones[0])