"""
Problem Statement#
Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.
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
    flip_me = False
    while q:
      q_len = len(q)
      level_arr = []
      for i in range(q_len):
        n = q.popleft()
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
        if flip_me:
          level_arr.insert(0, n.val)
        else:
          level_arr.append(n.val)
      flip_me = not flip_me
      result.append(level_arr)
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
