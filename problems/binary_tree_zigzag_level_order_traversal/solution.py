# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = collections.deque()
        q.append(root)
        toggle = False
        while q:
            ql = len(q)
            r = []
            for _ in range(ql):
                n = q.popleft()
                r.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if toggle:
                r = r[::-1]
            toggle = not toggle
            ans.append(r)
        return ans