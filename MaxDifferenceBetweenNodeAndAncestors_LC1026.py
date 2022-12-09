# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # Keep track of our biggest abs difference.
        biggest = 0
        # Helper func that track the min and max vals found in a path.
        def helper(node, maxx, minn):
            nonlocal biggest
            if not node:
                return
			# Update min and max 's comparing with current node.val.
            maxx = max(node.val, maxx) 
            minn = min(node.val, minn)
		    # Update our global biggest difference.
            biggest = max(biggest, abs(maxx - minn))
			# Recurse/traverse l and r subtrees.
            helper(node.left, maxx, minn)
            helper(node.right, maxx, minn)
            
        helper(root, root.val, root.val)
        
        return biggest