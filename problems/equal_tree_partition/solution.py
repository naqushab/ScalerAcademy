# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if root.left:
                set_node.add(l)
            if root.right:
                set_node.add(r)
            return l + r + root.val
        set_node = set()
        total = dfs(root)
        return (total%2 == 0 and total//2 in set_node)