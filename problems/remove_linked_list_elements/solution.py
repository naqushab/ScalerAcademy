# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        prev = ListNode(0)
        prev.next = head
        temp = prev.next
        dummy = prev
        while prev and temp:
            while temp and temp.val == val:
                temp = temp.next
            prev.next = temp
            if prev:
                prev = prev.next
            if temp:
                temp = temp.next
        return dummy.next