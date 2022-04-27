# Definition for a  binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None
import collections

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        q = collections.deque()
        ans = []
        if not A:
            return ans
        q.append(A)
        while q:
            ql = len(q)
            level = []
            for _ in range(ql):
                n = q.popleft()
                level.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            ans.append(level)
        return ans