# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == val:
            return root
        l, r = root.left, root.right
        if l and root.val > val:
            return self.searchBST(l, val)
        else:
            return self.searchBST(r, val)