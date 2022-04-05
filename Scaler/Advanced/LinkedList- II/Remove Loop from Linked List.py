# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        if not A:
            return A
        is_cycle_found, slow_ptr = self.is_cycle(A)
        if is_cycle_found:
            cycle_len = self.get_cycle_len(slow_ptr)
            slow = A
            fast = A
            for _ in range(cycle_len):
                fast = fast.next
            prev = A
            while slow != fast:
                prev = fast
                slow = slow.next
                fast = fast.next
            prev.next = None
        return A

    def is_cycle(self, A):
        slow = A
        fast = A
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True, slow
        return False, None

    def get_cycle_len(self, node):
        cur = node.next
        l = 1
        while cur != node:
            cur = cur.next
            l += 1
        return l