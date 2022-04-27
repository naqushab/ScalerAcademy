# Definition for a  binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        def check_sym(l, r):
            if not l and not r:
                return 1
            if not l or not r:
                return 0
            return int(l.val == r.val) and check_sym(l.left, r.right) and check_sym(l.right, r.left)

        if not A:
            return 1
        else:
            return check_sym(A.left, A.right)