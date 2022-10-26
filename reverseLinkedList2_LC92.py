# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1. find the left node
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head

        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
        
        # now cur = 'left', leftPrev = 'node before left'
        # 2. reverse the list from left to right
        prev = None

        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp

        # now cur = 'right + 1', prev = 'right'
        # 3. connect the leftPrev and prev
        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next



