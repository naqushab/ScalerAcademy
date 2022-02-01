# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    def isSymmetric(self, A):
        if not A:
            return 1
        
        def check_l_and_r(l, r):
            if not l and not r:
                return True
            elif not l or not r:
                return False
            return l.val == r.val and check_l_and_r(l.left, r.right) and check_l_and_r(l.right, r.left)
        
        return 1 if check_l_and_r(A.left, A.right) else 0