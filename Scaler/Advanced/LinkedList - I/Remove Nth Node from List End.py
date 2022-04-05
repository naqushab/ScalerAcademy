# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        l = self.get_len(A)
        if B > l:
            A = A.next
            return A
        else:
            ans = slow = ListNode(0)
            slow.next = A
            fast = A
            for _ in range(B):
                fast = fast.next
            while fast:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
            return ans.next
    
    def get_len(self, head):
        l = 0
        c = head
        while c:
            c = c.next
            l += 1
        return l