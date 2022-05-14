# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_bst(root, -math.inf, math.inf)
    
    def is_valid_bst(self, root, left, right):
        if not root:
            return True
        if left < root.val < right:
            left = self.is_valid_bst(root.left, left, root.val)
            right = self.is_valid_bst(root.right, root.val, right)
            return left and right
        else:
            return False