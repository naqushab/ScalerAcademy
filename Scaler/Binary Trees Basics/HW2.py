# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

import collections
import math

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        count = 0
        if not A:
            return count
        st = collections.deque()
        st.append((A, -math.inf))
        while st:
            n, v = st.pop()
            if n.val > v:
                count += 1
            if n.left:
                st.append((n.left, max(n.val, v)))
            if n.right:
                st.append((n.right, max(n.val, v)))
        return count