# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        st = collections.deque()
        st.append((root, 1))
        max_h = float('-inf')
        while st:
            n, h = st.pop()
            max_h = max(max_h, h)
            if n.left:
                st.append((n.left, h+1))
            if n.right:
                st.append((n.right, h+1))
        return max_h