# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                prev = dummy
                while prev.next.val < curr.next.val:
                    prev = prev.next
                temp = curr.next
                curr.next = curr.next.next
                temp.next = prev.next
                prev.next = temp
        return dummy.next
        
        
        # dummyNode = ListNode(0, head)

        # prev, cur = head, head.next

        # while cur:
        #     if cur.val >= prev.val:
        #         prev, cur = cur, cur.next
        #         continue

        #     tmp = head
        #     while cur.val > tmp.next.val:
        #         tmp = tmp.next

        #     prev.next = cur.next
        #     cur.next = tmp.next
        #     tmp.next = cur
        #     cur = prev.next

        # return dummyNode.next

        
