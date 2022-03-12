"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        old_to_new_map = {}
        cur = head
        while cur:
            new = Node(cur.val)
            old_to_new_map[cur] = new
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next:
                old_to_new_map[cur].next = old_to_new_map[cur.next]
            if cur.random:
                old_to_new_map[cur].random = old_to_new_map[cur.random]
            cur = cur.next
        
        return old_to_new_map[head]