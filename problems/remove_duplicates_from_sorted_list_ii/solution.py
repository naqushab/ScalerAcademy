# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = dummy = ListNode(0)
        ans.next = head
        cur = head
        while cur:
            if cur and cur.next and cur.val == cur.next.val:
                dup_val = cur.val
                while cur and cur.val == dup_val:
                    cur = cur.next
            else:
                ans.next = cur
                cur = cur.next
                ans = ans.next
        ans.next = cur
        return dummy.next