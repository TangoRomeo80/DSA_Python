# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # find the middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        prev = None
        curr = slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # merge two lists
        first = head
        second = prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next