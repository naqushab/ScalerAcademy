# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        def dfs(root):
            if not root:
                return None
            
            if not root.left and not root.right:
                return root
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            if l:
                l.right = root.right
                root.right = root.left
                root.left = None
            
            return r if r else l
        
        dfs(root)