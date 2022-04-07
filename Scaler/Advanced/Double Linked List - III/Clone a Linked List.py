"""
class ListNode: 
    def __init__(x):
        self.val = x
        self.next = None
        self.random = None
"""
def clonelist(A):
    old_to_new = {None:None}
    cur = A
    while cur:
        old_to_new[cur] = RandomListNode(cur.label)
        cur = cur.next
    cur = A
    while cur:
        old_to_new[cur].next = old_to_new[cur.next]
        old_to_new[cur].random = old_to_new[cur.random]
        cur = cur.next
    return old_to_new[A]