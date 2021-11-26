from collections import deque

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
  allPaths = []
  # TODO: Write your code here
  if not root:
    return allPaths
  else:
    q = deque()
    q.append(([root], sum-root.val))
    while q:
      n_list, d = q.pop()
      n = n_list[-1]
      if not n.left and not n.right and d == 0:
        tmp_arr = []
        for node in n_list:
          tmp_arr.append(node.val)
        allPaths.append(tmp_arr)
      if n.left:
        l = n_list + [n.left]
        q.append((l, d-n.left.val))
      if n.right:
        r = n_list + [n.right]
        q.append((r, d-n.right.val))
  return allPaths


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()
