# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if not descriptions:
            return None
        q = collections.deque()
        parents = collections.defaultdict(list)
        children_node = set()
        parents_node = set()
        for relationship in descriptions:
            parent, child, isLeft = relationship
            parents[parent].append((child, isLeft))
            children_node.add(child)
            parents_node.add(parent)
        root = parents_node-children_node
        root_val = root.pop()
        root = TreeNode(root_val)
        q.append(root)
        while q:
            node = q.pop()
            children = parents[node.val]
            if not children:
                continue
            if children[0][1] == 1:
                node.left = TreeNode(children[0][0])
                q.append(node.left)
            else:
                node.right = TreeNode(children[0][0])
                q.append(node.right)
            if len(children) > 1:
                if children[1][1] == 1:
                    node.left = TreeNode(children[1][0])
                    q.append(node.left)
                else:
                    node.right = TreeNode(children[1][0])
                    q.append(node.right)
        return root