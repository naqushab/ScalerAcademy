# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

import collections

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def solve(self, A):
        if not A:
            return None
        q = collections.deque()
        q.extend(A)
        parents = collections.deque()
        
        v = q.popleft()
        root = TreeNode(v)
        parents.append(root)
        
        while parents:
            pl = len(parents)
            for _ in range(pl):
                n = parents.popleft()
                l, r = q.popleft(), q.popleft()
                if l != -1:
                    n.left = TreeNode(l)
                    parents.append(n.left)
                if r != -1:
                    n.right = TreeNode(r)
                    parents.append(n.right)
        
        return root

if __name__ == '__main__':
    s = Solution()
    print(s.solve([ 1, 2, 3, 4, 5, -1, -1, -1, -1, -1, 6, -1, -1 ]))