# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = None
        s = head
        f = head
        for _ in range(1, n):
            f = f.next
        while f.next:
            p = s
            s = s.next
            f = f.next
        if s == head:
            head = s.next
        else:
            p.next = s.next
        return head
            