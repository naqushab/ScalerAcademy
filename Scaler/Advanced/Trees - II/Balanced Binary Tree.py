# Definition for a  binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        is_bal, hgt = self.isBalancedUtil(A)
        return int(is_bal)
    
    def isBalancedUtil(self, A):
        if not A:
            return True, -1
        l_bal, l_hgt = self.isBalancedUtil(A.left)
        r_bal, r_hgt = self.isBalancedUtil(A.right)
        return l_bal and r_bal and abs(l_hgt-r_hgt) <= 1, max(l_hgt, r_hgt) + 1