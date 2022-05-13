# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diameterOfBinaryTreeUtil(root).diameter
    
    def diameterOfBinaryTreeUtil(self, root):
        if not root:
            return TreeInfo(0, 0)
        left = self.diameterOfBinaryTreeUtil(root.left)
        right = self.diameterOfBinaryTreeUtil(root.right)
        return TreeInfo(max(left.diameter, right.diameter, left.height + right.height), max(left.height, right.height) + 1 )