# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def __lt__(self, other):
    return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = __lt__
        h = []
        for l in lists:
            if l:
                heapq.heappush(h, l)
        
        ans = dummy = ListNode(0)
        
        while h:
            n = heapq.heappop(h)
            ans.next = n
            n_next = n.next
            ans = ans.next
            ans.next = None
            if n_next:
                heapq.heappush(h, n_next)
        
        return dummy.next
            