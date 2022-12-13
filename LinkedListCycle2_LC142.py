# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return None
        # slow = head
        # fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         break
        # if not fast or not fast.next:
        #     return None
        # slow = head
        # while slow != fast:
        #     slow = slow.next
        #     fast = fast.next
        # return slow
        visited = {}
        while head:
            if head in visited:
                return head
            visited[head] = True
            head = head.next
        return None