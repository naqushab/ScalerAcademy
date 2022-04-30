# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#       self.val = x
#       self.next = None

import sys
sys.setrecursionlimit(10**9)

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        if not A or not A.next:
            return A
        prev = None
        slow = A
        fast = A
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        l2 = slow
        prev.next = None
        l1 = A
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        if l1.val <= l2.val:
            l3 = l1
            l1 = l1.next
        else:
            l3 = l2
            l2 = l2.next
        cur = l3
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return l3