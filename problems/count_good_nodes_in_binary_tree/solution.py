# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        q = deque()
        q.append((root, float('-inf')))
        while q:
            ql = len(q)
            for _ in range(ql):
                n, max_d = q.popleft()
                if n.val >= max_d:
                    ans += 1
                if n.left:
                    q.append((n.left, max(max_d, n.val)))
                if n.right:
                    q.append((n.right, max(max_d, n.val)))
        return ans