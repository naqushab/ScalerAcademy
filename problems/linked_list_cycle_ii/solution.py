# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s, f = head, head
        cycle = False
        while s:
            if f and f.next:
                f = f.next.next
            elif not f or not f.next:
                break
            s = s.next
            if s == f:
                cycle = True
                break
        if not cycle:
            return None
        
        h = s.next
        l = 1
        while h != s:
            h = h.next
            l += 1
        
        s, f = head, head
        while l > 0:
            f = f.next
            l -= 1

        while s != f:
            s = s.next
            f = f.next
        return s