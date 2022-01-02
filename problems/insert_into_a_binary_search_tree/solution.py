# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        
        def insert_iterative(node, val):
            cur = node
            prev = None
            while cur:
                prev = cur
                if cur.val >= val:
                    cur = cur.left
                else:
                    cur = cur.right
            if prev.val >= val:
                prev.left = TreeNode(val)
            else:
                prev.right = TreeNode(val)
        
        def insert(node, val):
            if not node.left and not node.right:
                if node.val >= val:
                    node.left = TreeNode(val)
                    return
                else:
                    node.right = TreeNode(val)
                    return
            if node.val >= val:
                if node.left:
                    insert(node.left, val)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    insert(node.right, val)
                else:
                    node.right = TreeNode(val)
        
        node = root
        insert(node, val)
        return root