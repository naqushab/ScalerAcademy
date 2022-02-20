# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = dummy = ListNode(0)
        node_sum = 0
        while head and head.val == 0:
            head = head.next
        while head:
            if head.val == 0 and node_sum > 0:
                ans.next = ListNode(node_sum)
                ans = ans.next
                node_sum = 0
            else:
                node_sum += head.val
                head = head.next
        return dummy.next
                