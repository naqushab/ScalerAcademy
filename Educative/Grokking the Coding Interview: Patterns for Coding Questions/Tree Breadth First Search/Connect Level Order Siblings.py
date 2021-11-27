"""
Problem Statement#
Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.
"""

from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()


def connect_level_order_siblings(root):
  # TODO: Write your code here
  if not root:
    return
  else:
    q = deque()
    q.append(root)
    while q:
      q_len = len(q)
      for i in range(q_len):
        a = q.popleft()
        if i < q_len-1:
          b = q[0]
        else:
          b = None
        a.next = b
        if a.left:
          q.append(a.left)
        if a.right:
          q.append(a.right)
  return

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()
