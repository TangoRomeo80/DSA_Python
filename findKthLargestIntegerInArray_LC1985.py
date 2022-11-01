import heapq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for num in nums:
            heapq.heappush(heap, -int(num))
        for i in range(k):
            res = heapq.heappop(heap)
        return str(-int(res))