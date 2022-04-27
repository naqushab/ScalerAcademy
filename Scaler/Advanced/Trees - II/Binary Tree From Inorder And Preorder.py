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
        self.index_map = {x: i for i, x in enumerate(B)}
        self.preorder = A
        self.inorder = B
        return self.buildTreeHelper(0, len(self.preorder)-1, 0, len(self.inorder)-1)

    def buildTreeHelper(self, preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_start > preorder_end:
            return None
        root_val = self.preorder[preorder_start]
        root = TreeNode(root_val)
        root_val_index = self.index_map[root_val]
        left_subtree_count = (root_val_index-1-inorder_start+1)
        root.left = self.buildTreeHelper(preorder_start+1, preorder_start + left_subtree_count, inorder_start, root_val_index-1)
        root.right = self.buildTreeHelper(preorder_start + left_subtree_count + 1, preorder_end, root_val_index+1, inorder_end)
        return root
