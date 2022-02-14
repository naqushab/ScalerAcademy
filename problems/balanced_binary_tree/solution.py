# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        return 1+max(l, r)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        height_l = self.height(root.left)
        height_r = self.height(root.right)
        return abs(height_l - height_r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)