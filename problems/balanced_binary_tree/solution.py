# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeInfo:
    def __init__(self, is_bal, height):
        self.is_bal = is_bal
        self.height = height

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.is_balanced(root).is_bal
    
    def is_balanced(self, root):
        if not root:
            return TreeInfo(True, 0)
        left = self.is_balanced(root.left)
        right = self.is_balanced(root.right)
        return TreeInfo(left.is_bal and right.is_bal and abs(left.height - right.height) <= 1, max(left.height, right.height)+1)