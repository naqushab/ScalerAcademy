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
        dia, ht = self.diameter(A)
        return dia

    def diameter(self, root):
        if not root:
            return -1, -1
        ld, lh = self.diameter(root.left)
        rd, rh = self.diameter(root.right)
        return max(ld, rd, lh+rh+2), max(lh, rh) + 1