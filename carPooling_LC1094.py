import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #O(n)
        passChange = [0] * 1001
        for trip in trips:
            numPass, start, end = trip
            passChange[start] += numPass
            passChange[end] -= numPass

        curPass = 0
        for i in range(1001):
            curPass += passChange[i]
            if curPass > capacity:
                return False

        return True


        #O(nlogn)
        # trips.sort(key = lambda x: x[1])
        # heap = [] #pair of (end, numPass)
        # curPass = 0
        # for trip in trips:
        #     numPass, start, end = trip
        #     while heap and heap[0][0] <= start:
        #         curPass -= heapq.heappop(heap)[1]
        #     curPass += numPass
        #     if curPass > capacity:
        #         return False
        #     heapq.heappush(heap, [end, numPass])
        # return True