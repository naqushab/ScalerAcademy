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
        self.index_map = {x: i for i, x in enumerate(A)}
        self.inorder = A
        self.postorder = B
        return self.buildTreeHelper(0, len(self.postorder)-1, 0, len(self.inorder)-1)

    def buildTreeHelper(self, postorder_start, postorder_end, inorder_start, inorder_end):
        if inorder_start > inorder_end:
            return None
        root_val = self.postorder[postorder_end]
        root = TreeNode(root_val)
        root_val_index = self.index_map[root_val]
        right_subtree_count = (inorder_end-(root_val_index+1)+1)
        root.left = self.buildTreeHelper(postorder_start, postorder_end - (right_subtree_count +1), inorder_start, root_val_index-1)
        root.right = self.buildTreeHelper(postorder_end - (right_subtree_count +1) + 1, postorder_end-1, root_val_index+1, inorder_end)
        return root