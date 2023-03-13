# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, path):
        if root is None:
            return
        path = (path << 1) | root.val
        if root.left is None and root.right is None:
            self.result += path
        self.dfs(root.left, path)
        self.dfs(root.right, path)