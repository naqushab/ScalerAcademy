# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        # middle
        slow = fast = A
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        #reverse
        prev, cur = None, slow
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        #merge
        first, second = A, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return  A