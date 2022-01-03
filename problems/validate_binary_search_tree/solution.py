# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def valid(n, l, r):
            if not n:
                return True
            return l < n.val < r and valid(n.left, l, n.val) and valid(n.right, n.val, r)
        
        return valid(root, -math.inf, math.inf)