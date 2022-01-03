# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(n, p, q):
            if not n:
                return
            if p.val < n.val > q.val:
                return lca(n.left, p, q)
            elif p.val > n.val < q.val:
                return lca(n.right, p, q)
            else:
                return n
        
        return lca(root, p, q)