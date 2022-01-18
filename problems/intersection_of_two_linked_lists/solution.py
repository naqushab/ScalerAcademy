# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_len(node):
            l = 0
            while node:
                l+=1
                node = node.next
            return l
        
        la, lb = get_len(headA), get_len(headB)
        
        if la >= lb:
            big = headA
            small = headB
        else:
            big = headB
            small = headA
        
        extra = abs(la-lb)
        
        while extra > 0:
            big = big.next
            extra -= 1
            
        while big and small:
            if big == small:
                return big
            big = big.next
            small = small.next
        
        return None