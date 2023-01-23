class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # initialize the slow, fast pointers to head and the prev to none for linked list reversal 
        slow, fast, prev = head, head, None
        # while there is fast next for it to jump to its next pointer 
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # linked list reversal 
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        # for comparison 
        fast, slow = head, prev
        # it will traverse until it hits the node in the middle with the NULL next 
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        # once middle is reached and there are no mismatches, then the linkedList is a palindrome 
        return True