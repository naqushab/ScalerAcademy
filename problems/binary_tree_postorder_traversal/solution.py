# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def recursive(root):
            if not root:
                return
            recursive(root.left)
            recursive(root.right)
            ans.append(root.val)
        
        def iterative(root):
            st = collections.deque()
            st.append(root)
            while st:
                n = st.pop()
                if n:
                    ans.insert(0, n.val)
                    st.append(n.left)
                    st.append(n.right)
            return ans
        #recursive(root)
        return iterative(root)