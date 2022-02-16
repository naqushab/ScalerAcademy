# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = dummy = ListNode(0)
        ans.next = head
        while head and head.next:
            temp = head.next
            nxt = temp.next
            ans.next = temp
            ans = ans.next
            head.next = None
            ans.next = head
            ans = ans.next
            head = nxt
        if head:
            ans.next = head
        return dummy.next