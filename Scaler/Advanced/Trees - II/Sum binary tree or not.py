# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        s, is_sum = self.sum_binary_tree(A)
        return int(is_sum)
    
    def sum_binary_tree(self, A):
        if not A:
            return 0, True
        if not A.left and not A.right:
            return A.val, True
        l_sum, is_sum_l = self.sum_binary_tree(A.left)
        r_sum, is_sum_r = self.sum_binary_tree(A.right)
        return (A.val+l_sum+r_sum), (A.val == l_sum+r_sum and is_sum_l and is_sum_r)