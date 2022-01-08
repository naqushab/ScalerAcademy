# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        res = 0
        l = len(ans)
        for i in range(0, l//2):
            res = max(res, ans[i]+ans[l-i-1])
        return res