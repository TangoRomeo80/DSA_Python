# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        #return pair: [rob root, not rob root]
        def dfs(root):
            if not root:
                return [0,0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            rob_root = root.val + left[1] + right[1]
            not_rob_root = max(left) + max(right)
            
            return [rob_root, not_rob_root]

        return max(dfs(root))