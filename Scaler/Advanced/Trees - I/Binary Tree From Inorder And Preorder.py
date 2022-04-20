# Definition for a  binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        index_m = {}
        for i, n in enumerate(B):
            index_m[n] = i
        return self.bt(index_m, A, B, 0, len(A)-1, 0, len(B)-1)
    
    def bt(self, index_m, A, B, pre_l, pre_r, in_l, in_r):
        if pre_l > pre_r:
            return None
        root = TreeNode(A[pre_l])
        inorder_index = index_m[A[pre_l]]
        count = inorder_index - 1 - in_l + 1
        root.left = self.bt(index_m, A, B, pre_l+1, pre_l + count, in_l, inorder_index-1)
        root.right = self.bt(index_m, A, B, pre_l + count + 1, pre_r, inorder_index+1, in_r)
        return root