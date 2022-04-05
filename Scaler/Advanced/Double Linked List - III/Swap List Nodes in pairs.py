# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def swapPairs(self, A):
        ans = dummy = ListNode(0)
        ans.next = A
        while A and A.next:
            n2n = A.next
            f = n2n.next
            n = A
            ans.next = n2n
            ans = ans.next
            ans.next = n
            ans = ans.next
            ans.next = None
            A = f
        if A:
            ans.next = A
        return dummy.next