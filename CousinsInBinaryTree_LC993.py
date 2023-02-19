# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        queue = [root]
        while queue:
            x_found = False
            y_found = False
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.val == x:
                    x_found = True
                if node.val == y:
                    y_found = True
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.left.val == y and node.right.val == x:
                        return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if x_found and y_found:
                return True
            if x_found or y_found:
                return False

