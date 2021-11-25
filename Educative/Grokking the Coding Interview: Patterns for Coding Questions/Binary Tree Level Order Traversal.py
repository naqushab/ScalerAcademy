"""
Problem Statement#
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  # TODO: Write your code here
  if not root:
    return result
  else:
    q = deque()
    q.append(root)
    while q:
      q_len = len(q)
      level_arr = []
      for i in range(q_len):
        n = q.popleft()
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
        level_arr.append(n.val)
      result.append(level_arr)
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
