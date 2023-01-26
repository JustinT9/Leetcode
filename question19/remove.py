# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next is None: 
            return None 
        elif head.next.next is None and n == 1: 
            head.next = None 
            return head 
        elif head.next.next is None and n == 2: 
            return head.next

        before, after = head, head.next.next

        i = 0
        while i < n:
            if before is not None:
                before = before.next
            if after is not None:
                after = after.next 
            i += 1

        if before is not None:
            before.next = after 
        return head 
    