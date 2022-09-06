class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(head):
        # if not head:
        #     return True
        # stack = []
        # curr = head
        # while curr:
        #     stack.append(curr.val)
        #     curr = curr.next
        # while stack:
        #     if stack.pop() != head.val:
        #         return False
        #     head = head.next
        # return True

        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        left, right = head, prev
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True