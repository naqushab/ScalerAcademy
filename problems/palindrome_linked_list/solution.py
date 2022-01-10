# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return head
        
        s, f = ListNode(0), head
        s.next = head
        while f and f.next:
            s = s.next
            f = f.next.next
            
        prev = s
        cur = prev.next
        prev.next = None
        p = None
        
        while cur:
            temp = cur.next
            cur.next = p
            p = cur
            cur = temp
        
        last = p
        first = head
        while first and last:
            if first.val != last.val:
                return False
            first = first.next
            last = last.next
        return True