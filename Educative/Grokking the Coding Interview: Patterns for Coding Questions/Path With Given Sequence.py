"""
Problem Statement#
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
"""

from collections import deque

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  # TODO: Write your code here
  if not root:
    if len(sequence) > 0:
      return False
    else:
      return True
  else:
    s = deque()
    s.append([root])
    while s:
      n_list = s.pop()
      n = n_list[-1]
      if not n.left and not n.right:
        if len(n_list) == len(sequence):
          seq_len = len(sequence)
          equal = True
          for s_i in range(seq_len):
            if n_list[s_i].val != sequence[s_i]:
              equal = False
          if equal:
            return True
      if n.left:
        l = n_list + [n.left]
        s.append(l)
      if n.right:
        r = n_list + [n.right]
        s.append(r)
  return False


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
