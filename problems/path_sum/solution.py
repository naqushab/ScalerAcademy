# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, targetSum)
    
    def dfs(self, A, B):
        if not A:
            return False
        if not A.left and not A.right:
            return A.val == B
        l = self.dfs(A.left, B-A.val)
        r = self.dfs(A.right, B-A.val)
        return l or r
    
    def bfs(self, root, targetSum):
        if not root:
            return False
        st = collections.deque()
        st.append((root, targetSum-root.val))
        while st:
            n, v = st.pop()
            if not n.left and not n.right and v == 0:
                return True
            if n.left:
                st.append((n.left, v-n.left.val))
            if n.right:
                st.append((n.right, v-n.right.val))
        return False