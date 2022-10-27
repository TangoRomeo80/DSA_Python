class Solution:
    def numTrees(self, n: int) -> int:
        #numTrees(n) = sum(numTrees(i-1) * numTrees(n-i)) for i in range(1,n+1) 
        #numTrees(0) = 1
        #numTrees(1) = 1

        numTree = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += numTree[root - 1] * numTree[nodes - root]
            numTree[nodes] = total
        return numTree[n]