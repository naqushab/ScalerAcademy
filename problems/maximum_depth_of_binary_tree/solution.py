# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0
            l = node.left
            r = node.right
            return max(height(l), height(r)) + 1
        return height(root)