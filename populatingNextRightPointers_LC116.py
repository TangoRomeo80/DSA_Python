
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #BFS solution
        # if not root:
        #     return None
        # queue = [root]
        # while queue:
        #     size = len(queue)
        #     for i in range(size):
        #         node = queue.pop(0)
        #         if i < size - 1:
        #             node.next = queue[0]
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return root

        #DFS solution
        cur, nxt = root, root.left if root else None

        while cur and nxt:
            cur.left.next = cur.right
            cur.right.next = cur.next.left if cur.next else None
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return root
