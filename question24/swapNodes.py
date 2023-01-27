# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# done in 32m 
class Solution(object):
    def swapPairs(self, head):
        if head is None: 
            return head 
        elif head.next is None: 
            return head
        else: 
            lPtr, rPtr, head, prev = head, head.next, head.next, head 
            while lPtr and lPtr.next: 
                lPtr.next = rPtr.next
                rPtr.next = lPtr
                lPtr = lPtr.next
                if lPtr and lPtr.next: 
                    rPtr = lPtr.next 
                    prev.next = rPtr
                    prev = lPtr

        return head 