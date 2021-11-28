"""
Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.
"""

from collections import deque

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class TreeDiameter:

  def __init__(self):
    self.treeDiameter = 0

  def find_diameter_node(self, root, d):
    if not root:
      return d
    else:
      s = deque()
      dia = 0
      s.append((root, d))
      while s:
        n, d = s.pop()
        dia = max(d, dia)
        if n.left:
          s.append((n.left, d+1))
        if n.right:
          s.append((n.right, d+1))
    return dia

  def find_diameter(self, root):
    # TODO: Write your code here
    if not root:
      return 0
    else:
      s = deque()
      max_dia = 1
      s.append((root, max_dia))
      while s:
        n, d = s.pop()
        max_dia = max(self.find_diameter_node(n.left, d)+self.find_diameter_node(n.right, d)+1, max_dia)
        if n.left:
          s.append((n.left, 1))
        if n.right:
          s.append((n.right, 1))
    return max_dia

def main():
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()
