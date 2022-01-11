# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        if not root:
            return 0
        def todecimal(arr):
            p = 0
            num = 0
            for i in range(len(arr)-1, -1, -1):
                num += arr[i]*pow(2, p)
                p+=1
            return num
            
        def dfs(root):
            st = collections.deque()
            st.append((root, [root.val]))
            while st:
                node, num = st.pop()
                if not node.left and not node.right:
                    self.ans += todecimal(num[:])
                if node.right:
                    st.append(( node.right, num + [node.right.val] ))
                if node.left:
                    st.append(( node.left, num + [node.left.val] ))
        
        dfs(root)
        return self.ans