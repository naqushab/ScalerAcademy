# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = []
        head = root
        def inorder(head):
            if not head:
                return
            inorder(head.left)
            l.append(head.val)
            inorder(head.right)
            
        inorder(head)
        s, e = 0, len(l)-1
        if s == e:
            return False
        while s < e:
            sm = l[s]+l[e]
            if sm == k:
                return True
            elif sm < k:
                s += 1
            else:
                e -= 1
        return False