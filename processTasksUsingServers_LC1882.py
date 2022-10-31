import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # two min heaps, one for available servers, one for unavailable servers
        #available = (weight, index)
        #unavailable = (timeNextAvailable, weight, index)

        res = [0] * len(tasks)

        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)
        unavail = []

        t = 0
        for i, task in enumerate(tasks):
            t = max(t, i)
            # check if any server is available
            if len(available) == 0:
                t = unavail[0][0]
            while unavail and t >= unavail[0][0]:
                timeNextAvailable, weight, index = heapq.heappop(unavail)
                heapq.heappush(available, (weight, index))

            # assign task to available server
            weight, index = heapq.heappop(available)
            res[i] = index
            heapq.heappush(unavail, (t + task, weight, index))

        return res
