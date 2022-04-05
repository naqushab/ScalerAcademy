# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        s = A
        f = A
        while f and f.next:
            s = s.next
            f = f.next.next
        return s.val