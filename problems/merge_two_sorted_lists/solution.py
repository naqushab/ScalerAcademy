# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
                prev = prev.next
                prev.next = None
            else:
                prev.next = list2
                list2 = list2.next
                prev = prev.next
                prev.next = None
        if list1:
            prev.next = list1
        if list2:
            prev.next = list2
        return dummy.next