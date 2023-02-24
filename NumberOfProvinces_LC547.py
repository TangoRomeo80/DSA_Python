class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(isConnected, visited, i)
                count += 1
        return count

    def dfs(self, isConnected, visited, i):
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                visited[j] = True
                self.dfs(isConnected, visited, j)
