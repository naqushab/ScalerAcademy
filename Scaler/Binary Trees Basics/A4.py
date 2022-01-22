# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        if not A:
            return 0
        st = deque()
        st.append([A, 1])
        h = 0
        while st:
            n, d = st.pop()
            h = max(h, d)
            if n.left:
                st.append([n.left, d+1])
            if n.right:
                st.append([n.right, d+1])
        return h