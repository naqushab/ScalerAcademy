# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 1->2->3
        
        # rem = 2 in 2->3
        rem = head.next
        # 1->NULL
        head.next = None
        
        # p =3 in 3->2
        p = self.reverseList(rem)
        
        # .... 2->1
        rem.next = head
        
        return p