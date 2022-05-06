# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys
sys.setrecursionlimit(10**9)
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        def dfs(A):
            if not A:
                return 0
            l = dfs(A.left)
            r = dfs(A.right)
            if A.left:
                s.add(l)
            if A.right:
                s.add(r)
            return l+r+A.val
        s = set()
        total = dfs(A)
        return int(total%2 == 0 and total//2 in s)