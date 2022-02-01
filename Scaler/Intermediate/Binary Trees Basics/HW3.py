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
        count = 0
        if not A:
            return count
        st = collections.deque()
        st.append(A)
        while st:
            n = st.pop()
            if n:
                count += 1
                st.append(n.left)
                st.append(n.right)
        return count