# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr = []
        list1, list2 = [], []
        def inorder(node, arr):
            if not node:
                return []
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)
        
        inorder(root1, list1)
        inorder(root2, list2)
        
        i, j = 0, 0
        n1, n2 = len(list1), len(list2)
        while i < n1 or j < n2:
            if i < n1 and j < n2 and list1[i] <= list2[j]:
                arr.append(list1[i])
                i += 1
            elif i < n1 and j < n2 and list1[i] > list2[j]:
                arr.append(list2[j])
                j += 1
            elif i < n1:
                arr.append(list1[i])
                i += 1
            elif j < n2:
                arr.append(list2[j])
                j += 1
        return arr