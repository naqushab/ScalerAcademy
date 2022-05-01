# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import sys
sys.setrecursionlimit(10**9)

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list

    def merge2Lists(self, h1, h2):
        if not h1 and not h2:
            return h1
        elif not h1:
            return h2
        elif not h2:
            return h1
        if h1.val <= h2.val:
            h1.next = self.merge2Lists(h1.next, h2)
            return h1
        else:
            h2.next = self.merge2Lists(h1, h2.next)
            return h2

    def mergeKLists(self, A):
        n = len(A)
        if n == 1:
            return A[0]
        mid = n//2
        l = self.mergeKLists(A[:mid])
        r = self.mergeKLists(A[mid:])
        return self.merge2Lists(l, r)