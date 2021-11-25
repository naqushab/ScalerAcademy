"""
Problem Statement#
Given a binary tree, populate an array to represent the averages of all of its levels.

"""

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []
  # TODO: Write your code here
  if not root:
    return result
  else:
    q = deque()
    q.append(root)
    while q:
      q_len = len(q)
      s = 0
      for _ in range(q_len):
        n = q.popleft()
        s += n.val
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
      result.append(s/q_len)
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()







