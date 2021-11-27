"""
Problem Statement#
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
"""

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  # TODO: Write your code here
  if not root:
    return None
  else:
    q = deque()
    q.append(root)
    is_successor = False
    while q:
      q_len = len(q)
      for _ in range(q_len):
        n = q.popleft()
        if is_successor:
          return n
        if n.val == key:
          is_successor = True
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
  return None


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()
