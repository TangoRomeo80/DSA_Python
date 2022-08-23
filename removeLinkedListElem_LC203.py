# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         if not head:
#             return head
#         while head and head.val == val:
#             head = head.next
#         if not head:
#             return head
#         cur = head
#         while cur.next:
#             if cur.next.val == val:
#                 cur.next = cur.next.next
#             else:
#                 cur = cur.next
        
#         return head

        dummy = ListNode(next=head)
        prev,cur = dummy, head
        
        while cur:
            next = cur.next
            
            if cur.val == val:
                prev.next = next
            else:
                prev = cur
                
            cur = next
        
        return dummy.next