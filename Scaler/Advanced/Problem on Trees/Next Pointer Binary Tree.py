# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return root
        level = root
        while level:
            cur = level
            while cur:
                if cur.left:
                    if cur.right:
                        cur.left.next = cur.right
                    else:
                        cur.left.next = self.get_next_child(cur.next)
                if cur.right:
                    cur.right.next = self.get_next_child(cur.next)
                cur = cur.next
            if level.left:
                level = level.left
            elif level.right:
                level = level.right
            else:
                level = self.get_next_child(level.next)
    
    def get_next_child(self, node):
        while node:
            if node.left:
                return node.left
            if node.right:
                return node.right
            node = node.next
        return None