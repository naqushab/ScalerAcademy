# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        q = collections.deque()
        q.append(root)
        while q:
            ql = len(q)
            for i in range(ql):
                n = q.popleft()
                if n == u:
                    if i == ql-1:
                        return None
                    else:
                        return q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return None