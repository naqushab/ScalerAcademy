# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def recursive(root):
            if not root:
                return
            ans.append(root.val)
            recursive(root.left)
            recursive(root.right)
        
        def iterative(root):
            st = collections.deque()
            st.append(root)
            while st:
                n = st.pop()
                ans.append(n.val)
                if n.right:
                    st.append(n.right)
                if n.left:
                    st.append(n.left)
            return ans
        
        # recursive(root)
        return iterative(root) if root else []