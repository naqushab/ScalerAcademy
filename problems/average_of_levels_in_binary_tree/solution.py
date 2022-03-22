# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        if not root:
            return ans
        q = collections.deque()
        q.append(root)
        while q:
            ql = len(q)
            s = 0
            for _ in range(ql):
                v = q.popleft()
                s += v.val
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
            ans.append(s/ql)
        return ans