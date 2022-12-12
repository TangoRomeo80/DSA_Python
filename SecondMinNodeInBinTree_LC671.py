# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        res = set()
        def dfs(node):
            if node:
                res.add(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        res = sorted(res)
        return res[1] if len(res) > 1 else -1