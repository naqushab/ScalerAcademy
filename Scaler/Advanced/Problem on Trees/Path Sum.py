# Definition for a  binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        return int(self.dfs(A, B))
    
    def dfs(self, A, B):
        if not A:
            return False
        if not A.left and not A.right:
            return A.val == B
        l = self.dfs(A.left, B-A.val)
        r = self.dfs(A.right, B-A.val)
        return l or r