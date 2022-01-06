# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = float('-inf')
        def height(node):
            if not node:
                return 0
            l = node.left
            r = node.right
            return max(height(l), height(r)) + 1
        
        def diameter(node):
            if not node:
                return 0
            return max(height(node.left)+height(node.right), 
                      diameter(node.left), diameter(node.right))
        
        return diameter(root)