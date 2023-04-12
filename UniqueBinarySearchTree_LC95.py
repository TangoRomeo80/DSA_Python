# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None]
        allTrees = []
        for i in range(start, end + 1):
            leftTrees = self.helper(start, i - 1)
            rightTrees = self.helper(i + 1, end)
            for l in leftTrees:
                for r in rightTrees:
                    currTree = TreeNode(i)
                    currTree.left = l
                    currTree.right = r
                    allTrees.append(currTree)
        return allTrees
