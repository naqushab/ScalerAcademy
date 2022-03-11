# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        if k == 0:
            return head
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        k = k % l
        if k == 0:
            return head
        end = head
        new_head = None
        skips = l - k -1
        for _ in range(skips):
            end = end.next
        new_head = end.next
        end_iter = end.next
        end.next = None
        prev_head = head
        while end_iter.next:
            end_iter = end_iter.next
        end_iter.next = prev_head
        return new_head