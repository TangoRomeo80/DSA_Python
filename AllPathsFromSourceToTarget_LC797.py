class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        self.res = []
        self.dfs(graph, 0, [0])
        return self.res

    def dfs(self, graph, node, path):
        if node == len(graph) - 1:
            self.res.append(path)
            return
        for nei in graph[node]:
            self.dfs(graph, nei, path + [nei])

            