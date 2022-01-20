# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.append((root, 1))
        ans = math.inf
        while q:
            ql = len(q)
            for _ in range(ql):
                n, d = q.popleft()
                if not n.left and not n.right:
                    ans = min(ans, d)
                if n.left:
                    q.append((n.left, d+1))
                if n.right:
                    q.append((n.right, d+1))
        return ans
                