# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        q.append((root, targetSum-root.val, [root.val]))
        ans = []
        while q:
            ql = len(q)
            for _ in range(ql):
                n, s, arr = q.popleft()
                if not n.left and not n.right and s == 0:
                    ans.append(arr)
                if n.left:
                    new_arr = arr + [n.left.val]
                    q.append((n.left, s-n.left.val, new_arr))
                if n.right:
                    new_arr = arr + [n.right.val]
                    q.append((n.right, s-n.right.val, new_arr))
        return ans