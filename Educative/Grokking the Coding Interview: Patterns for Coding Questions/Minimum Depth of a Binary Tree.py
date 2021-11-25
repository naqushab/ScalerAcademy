"""
Problem Statement#
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  # TODO: Write your code here
  if not root:
    return 0
  else:
    q = deque()
    q.append(root)
    level = 0
    while q:
      level += 1
      q_len = len(q)
      for _ in range(q_len):
        n = q.popleft()
        if not n.left and not n.right:
          return level
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
  return -1


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
