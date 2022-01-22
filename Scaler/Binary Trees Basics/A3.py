# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
import collections

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def postorderTraversal(self, A):
        ans = []
        if not A:
            return ans
        st = collections.deque()
        st.append(A)
        while st:
            n = st.pop()
            ans.insert(0, n.val)
            if n.left:
                st.append(n.left)
            if n.right:
                st.append(n.right)
        return ans