# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        ptr = ans
        p1 = list1
        p2 = list2
        while p1 or p2:
            if p1 and p2:
                if p1.val <= p2.val:
                    ptr.next = p1
                    p1 = p1.next
                    ptr = ptr.next
                    ptr.next = None
                else:
                    ptr.next = p2
                    p2 = p2.next
                    ptr = ptr.next
                    ptr.next = None
            elif p1:
                ptr.next = p1
                p1 = p1.next
                ptr = ptr.next
                ptr.next = None
            elif p2:
                ptr.next = p2
                p2 = p2.next
                ptr = ptr.next
                ptr.next = None
        return ans.next