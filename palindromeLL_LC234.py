class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(head):
        if not head:
            return True
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        while stack:
            if stack.pop() != head.val:
                return False
            head = head.next
        return True