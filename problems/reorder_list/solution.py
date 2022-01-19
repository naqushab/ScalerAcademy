# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        q = collections.deque()
        nxt = head.next
        while nxt:
            q.append(nxt)
            nxt = nxt.next
        ans = head
        use_last = True
        while q:
            if use_last:
                ans.next = q.pop()
                ans = ans.next
                use_last = not use_last
            else:
                ans.next = q.popleft()
                ans = ans.next
                use_last = not use_last
        ans.next = None
        return