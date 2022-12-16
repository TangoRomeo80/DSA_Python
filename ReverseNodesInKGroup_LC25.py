# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        # find the k+1 node
        ptr = head
        for i in range(k):
            if not ptr:
                return head
            ptr = ptr.next
        # reverse list with k+1 node as head
        new_head = self.reverse(head, ptr)
        # reverse the rest
        head.next = self.reverseKGroup(ptr, k)
        return new_head

    def reverse(self, head, tail):
        prev = tail
        while head != tail:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev