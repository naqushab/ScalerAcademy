# Definition for a  binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None
import sys
sys.setrecursionlimit(10**9)

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        self.index_map = {}
        for i, n in enumerate(A):
            self.index_map[n] = i
        self.inorder, self.postorder = A, B
        return self.buildTreeUtil(0, len(A)-1, 0, len(B)-1)
    
    def buildTreeUtil(self, inorder_start, inorder_end, postorder_start, postorder_end):
        if inorder_start > inorder_end:
            return None
        root_val = self.postorder[postorder_end]
        root = TreeNode(root_val)
        inorder_root_index = self.index_map[root_val]
        right_subtree_count = inorder_end + 1 - inorder_root_index + 1
        root.left = self.buildTreeUtil(inorder_start, inorder_root_index-1, postorder_start, postorder_end - ( inorder_end - inorder_root_index +1))
        root.right = self.buildTreeUtil(inorder_root_index+1, inorder_end, postorder_end-1 - right_subtree_count, postorder_end-1)
        return root