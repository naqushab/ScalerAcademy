# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
    def lPalin(self, A):
        slow, fast = ListNode(0), A
        slow.next = A
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        p1, p2 = A, prev
        while p1:
            if p1.val != p2.val:
                return 0
            p1 = p1.next
            p2 = p2.next
        return 1