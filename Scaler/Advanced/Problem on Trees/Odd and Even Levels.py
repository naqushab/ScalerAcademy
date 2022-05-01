# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import collections

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        ans = 0
        if not A:
            return ans
        q = collections.deque()
        odd = True
        q.append(A)
        while q:
            ql = len(q)
            for _ in range(ql):
                n = q.popleft()
                if odd:
                    ans += n.val
                else:
                    ans -= n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            odd = not odd
        return ans