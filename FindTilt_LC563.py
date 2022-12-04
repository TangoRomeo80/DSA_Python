# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        t = 0
        def tilt(root):
            nonlocal t
            if not root:
                return 0
            left = tilt(root.left)
            right = tilt(root.right)
            t += abs(left - right)
            return left + right + root.val
        tilt(root)
        return t