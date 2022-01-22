# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def inorderTraversal(self, A):
        ans = []
        if not A:
            return ans
        st = deque()
        node = A
        while st or node:
            while node:
                st.append(node)
                node = node.left
            node = st.pop()
            ans.append(node.val)
            node = node.right
        return ans