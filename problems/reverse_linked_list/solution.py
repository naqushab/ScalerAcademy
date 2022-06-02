# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        rev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rev
    
    def rev(self, head):
        prev, cur = None, head
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        return prev