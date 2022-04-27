# Definition for a  binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        if self.search_key_present(A, B) and self.search_key_present(A, C):
            ans = self.lca_util(A, B, C)
            return ans.val
        else:
            return -1
    
    def search_key_present(self, A, key):
        if not A:
            return False
        if A.val == key:
            return True
        return self.search_key_present(A.left, key) or self.search_key_present(A.right, key)

    def lca_util(self, A, B, C):
        if not A:
            return None
        if A.val == B or A.val == C:
            return A
        l = self.lca_util(A.left, B, C)
        r = self.lca_util(A.right, B, C)
        if l and r:
            return A
        return l or r