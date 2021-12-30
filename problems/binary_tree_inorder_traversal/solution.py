# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def recursive(root):
            if not root:
                return
            recursive(root.left)
            ans.append(root.val)
            recursive(root.right)
            
        def iterative(root):
            st = collections.deque()
            c = root
            while st or c:
                while c:
                    st.append(c)
                    c = c.left
                c = st.pop()
                ans.append(c.val)
                c = c.right
            return ans
        #recursive(root)
        return iterative(root)