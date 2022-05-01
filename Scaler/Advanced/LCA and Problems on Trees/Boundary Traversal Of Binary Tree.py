# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

import collections

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def __init__(self):
        self.ans = []

    def left_boundary(self, root):
        if not root or (not root.left and not root.right): # null or leaf
            return
        if root:
            self.ans.append(root.val)
        if not root.left:
            self.left_boundary(root.right)
        else:
            self.left_boundary(root.left)

    def right_boundary(self, root):
        if not root or (not root.left and not root.right): # null or leaf
            return
        if not root.right:
            self.right_boundary(root.left)
        else:
            self.right_boundary(root.right)
        if root:
            self.ans.append(root.val)

    def leaves(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.ans.append(root.val)
        self.leaves(root.left)
        self.leaves(root.right)
        
    
    def solve(self, A):
        if not A:
            return self.ans
        self.ans.append(A.val)
        self.left_boundary(A.left)
        self.leaves(A.left)
        self.leaves(A.right)
        self.right_boundary(A.right)
        return self.ans