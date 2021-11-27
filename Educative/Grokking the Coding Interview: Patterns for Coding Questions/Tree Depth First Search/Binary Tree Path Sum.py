"""
Problem Statement#
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
"""

from collections import deque

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def dfs(node, sum):
  if not node:
    return False
  sum -= node.val
  if not node.left and not node.right:
    return sum == 0
  return dfs(node.left, sum) or dfs(node.right, sum)

def dfs_iterative(root, sum):
  if not root:
    return False
  else:
    q = deque()
    q.append((root, sum-root.val))
    while q:
      n, v = q.pop()
      if v == 0 and not n.left and not n.right:
        return True
      if n.left:
        q.append((n.left, v-n.left.val))
      if n.right:
        q.append((n.right, v-n.right.val))
    return False

def has_path(root, sum):
  # TODO: Write your code here
  return dfs_iterative(root, sum)

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()


