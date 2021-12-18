# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, ans):
        if not root:
            return
        ans.append(root.val)
        self.preorder(root.left, ans)
        self.preorder(root.right, ans)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.preorder(root, ans)
        return ans