"""
Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
"""

from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_right_view(root):
  result = []
  # TODO: Write your code here
  if not root:
    return result
  else:
    q = deque()
    q.append(root)
    while q:
      q_len = len(q)
      for i in range(q_len):
        n = q.popleft()
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
        if i == q_len -1:
          result.append(n)
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()







