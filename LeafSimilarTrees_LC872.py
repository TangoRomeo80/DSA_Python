# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        res = []
        dfs(root1)
        res1 = res
        res = []
        dfs(root2)
        res2 = res
        return res1 == res2