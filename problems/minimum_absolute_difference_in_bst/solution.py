# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.ans.append(root.val)
            self.inorder(root.right)
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        ans = math.inf
        for i in range(1, len(self.ans)):
            ans = min(ans, self.ans[i]-self.ans[i-1])
        return ans