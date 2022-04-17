# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def reverseList(self, A, B):
        if B <= 1 or not A:
            return A
        cur, prev = A, None
        k = B
        while cur and B > 0:
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp
            B -= 1
        A.next = self.reverseList(cur, k)
        return prev