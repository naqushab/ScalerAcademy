# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def deleteDuplicates(self, A):
        if not A:
            return None
        ans = dummy = ListNode(0)
        ans.next = A
        prev_val = None
        cur = A
        while cur:
            if prev_val is None or prev_val != cur.val:
                prev_val = cur.val
                ans.next = cur
                cur = cur.next
                ans = ans.next
                ans.next = None
            else:
                cur = cur.next
        return dummy.next