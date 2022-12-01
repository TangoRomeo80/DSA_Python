# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def trackMin(node, high, low):
            if not node:
                return high - low
            left = trackMin(node.left, node.val, low)
            right = trackMin(node.right, high, node.val)
            return min(left, right)
        return trackMin(root, float('inf'), float('-inf'))