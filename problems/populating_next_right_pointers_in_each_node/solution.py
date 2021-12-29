"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        leftMost = root
        while leftMost:
            lm = leftMost
            if lm.left:
                lm.left.next = lm.right
                prev_lm_right = lm.right
                lm = lm.next
                while lm:
                    prev_lm_right.next = lm.left
                    lm.left.next = lm.right
                    prev_lm_right = lm.right
                    lm = lm.next
            leftMost = leftMost.left
        return root