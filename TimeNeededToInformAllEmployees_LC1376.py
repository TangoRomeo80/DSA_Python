class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # build a tree
        tree = {}
        for i in range(n):
            if i == headID:
                continue
            if manager[i] not in tree:
                tree[manager[i]] = []
            tree[manager[i]].append(i)
        
        # bfs
        queue = [(headID, informTime[headID])]
        max_time = 0
        while queue:
            node, time = queue.pop(0)
            if node not in tree:
                max_time = max(max_time, time)
            else:
                for child in tree[node]:
                    queue.append((child, time + informTime[child]))
        return max_time