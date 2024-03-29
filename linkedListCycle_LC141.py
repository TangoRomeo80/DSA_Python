# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(head):
        visited = {}
        while head:
            if head in visited:
                return True
            visited[head] = True
            head = head.next
        return False