# Definition for a  binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

import collections

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        q = collections.deque()
        ans = []
        if not A:
            return ans
        q.append((A, 0))
        dist_map = collections.defaultdict(list)
        while q:
            ql = len(q)
            for _ in range(ql):
                n, d = q.popleft()
                dist_map[d].append(n.val)
                if n.left:
                    q.append((n.left, d-1))
                if n.right:
                    q.append((n.right, d+1))
        for k in sorted(dist_map.keys()):
            ans.append(dist_map[k])
        return ans