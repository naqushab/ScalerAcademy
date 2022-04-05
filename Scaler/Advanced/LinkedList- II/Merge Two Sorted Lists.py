# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A.val <= B.val:
            C = A
            A = A.next
        else:
            C = B
            B = B.next
        ans = C
        while A and B:
            if A.val <= B.val:
                ans.next = A
                A = A.next
            else:
                ans. next = B
                B = B.next
            ans = ans.next
        if A:
            ans.next = A
        if B:
            ans.next = B
        return C