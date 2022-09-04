# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root, k):
        d = {}
        
        def traverse(root, k):
            if not root:
                return False
            if k - root.val in d:
                return True
            else:
                d[root.val] = 1
                return traverse(root.left, k) or traverse(root.right, k)
                
        return traverse(root, k)