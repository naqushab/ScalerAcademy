# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        ans = C = ListNode(0)
        carry = 0
        while A or B or carry:
            if A:
                carry += A.val
                A = A.next
            if B:
                carry += B.val
                B = B.next
            d = carry % 10
            carry = carry // 10
            C.next = ListNode(d)
            C = C.next
        if carry:
            C.next = ListNode(carry)
            C = C.next
        return ans.next