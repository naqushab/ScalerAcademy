# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.depth = -1   
#        self.left = None
#        self.right = None
import sys
sys.setrecursionlimit(10**9)
import collections

class Solution:
    # @param A : root node of tree
    def solve(self, A):
        if not A:
            return
        q = collections.deque()
        q.append(A)
        depth = 1
        while q:
            ql = len(q)
            for _ in range(ql):
                n = q.popleft()
                n.depth = depth
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            depth += 1