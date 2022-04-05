# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        if B == C:
            return A
        ans = left_ptr = ListNode(0)
        left_ptr.next = A
        right_ptr = A
        for _ in range(B-1):
            left_ptr = left_ptr.next
        for _ in range(C):
            right_ptr = right_ptr.next
        
        first = cur = left_ptr.next
        left_ptr.next = None
        prev = None

        for _ in range(C-B+1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        left_ptr.next = prev
        first.next = right_ptr

        return ans.next