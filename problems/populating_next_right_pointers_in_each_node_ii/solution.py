"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            ql = len(q)
            prev = None
            for _ in range(ql):
                n = q.popleft()
                if not prev:
                    prev = n
                else:
                    prev.next = n
                    prev = prev.next
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return root