# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # res = []

        # def inorder(root):
        #     if root:
        #         inorder(root.left)
        #         res.append(root.val)
        #         inorder(root.right)

        # inorder(root)
        # return res[k - 1]

        #inorder solutions
        res = []

        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)

        inorder(root)
        return res[k - 1]
            