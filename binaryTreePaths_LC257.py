# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        paths = []
        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + "->" + path)
        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + "->" + path)
        return paths
    
    