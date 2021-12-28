# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        left_node, right_node = ListNode(0), head
        ans = left_node
        left_node.next = head
        k = right - left + 1
        while left > 1:
            left_node = left_node.next
            left -= 1
        while right > 0:
            right_node = right_node.next
            right -= 1
        
        first_reverse = prev = left_node.next
        cur = prev.next
        prev.next = None
        
        for _ in range(k-1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        left_node.next = prev
        first_reverse.next = right_node
        return ans.next