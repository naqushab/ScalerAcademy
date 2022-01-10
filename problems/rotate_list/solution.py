# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        prev_head = head
        # calculate l
        l = 0
        p = head
        while p:
            l += 1
            p = p.next
        # move to n-k
        k = k%l
        if k == 0 or k == l:
            return head
        
        p = head
        i = l-k
        for _ in range(i-1):
            p = p.next
        
        new_tail = p
        new_head = p.next
        if not new_head:
            return head
        else:
            new_tail.next = None
            n = new_head
            while n.next:
                n = n.next
            n.next = prev_head
            return new_head