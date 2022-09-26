# class UnionFind:
#     def __init__(self):
#         self.f = {}

#     def findParent(self, x):
#         y = self.f.get(x, x)
#         if x != y:
#             y = self.f[x] = self.findParent(y)
#         return y

#     def union(self, x, y):
#         self.f[self.findParent(x)] = self.findParent(y)


# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         dsu = UnionFind()
#         for a, b in edges:
#             dsu.union(a, b)
#         return len(set(dsu.findParent(x) for x in range(n)))

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = par[n1]

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res
