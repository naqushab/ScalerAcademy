"""
Problem Statement#
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
Read - https://leetcode.com/problems/path-sum-iii/solution/
"""


from collections import deque

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def count_path_util(root, S):
  if not root:
    return 0
  else:
    s = deque()
    count = 0
    s.append((root, S-root.val))
    while s:
      n, d = s.pop()
      if d == 0:
        count += 1
      if n.left:
        s.append((n.left, d-n.left.val))
      if n.right:
        s.append((n.right, d-n.right.val))
    return count


def count_paths(root, S):
  # TODO: Write your code here
  if not root:
    return 0
  else:
    s = deque()
    count = 0
    s.append((root, S-root.val))
    while s:
      n, d = s.pop()
      count += count_path_util(n, d)
      if n.left:
        s.append((n.left, S))
      if n.right:
        s.append((n.right, S))
    return count


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
