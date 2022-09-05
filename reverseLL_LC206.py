class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(head):
        # if not head:
        #     return None
        # prev = None
        # curr = head
        # while curr:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # return prev
        
        #stack implementation
        # if not head:
        #     return None
        
        # s = []
        # curr = head
        # while curr:
        #     s.append(curr.val)
        #     curr = curr.next
        # newHead = ListNode(s.pop())
        # dummy = ListNode(next=newHead)
        # while s:
        #     newHead.next = ListNode(s.pop())
        #     newHead = newHead.next
            
        # return dummy.next

        #recursive implementation

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead


        