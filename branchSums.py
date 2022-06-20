class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    def traverse(node, current_sum):
        if node is None:
            return
        current_sum += node.value
        if node.left is None and node.right is None:
            sums.append(current_sum)
            return
        traverse(node.left, current_sum)
        traverse(node.right, current_sum)
    traverse(root, 0)
    return sums