# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import collections

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        ans = 0
        if not A:
            return ans
        q = collections.deque()
        q.append(A)
        while q:
            n = q.popleft()
            ans = max(ans, n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return ans