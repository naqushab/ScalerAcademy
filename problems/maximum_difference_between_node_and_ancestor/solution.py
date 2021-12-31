# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        st = collections.deque()
        max_ans_val = min_ans_val = root.val
        st.append((root, max_ans_val, min_ans_val))
        max_v = float('-inf')
        
        while st:
            n, max_ans_val, min_ans_val = st.pop()
            v1 = abs(max_ans_val - n.val)
            v2 = abs(min_ans_val - n.val)
            max_v = max(max_v, v1)
            max_v = max(max_v, v2)
            max_ans_val = max(max_ans_val, n.val)
            min_ans_val = min(min_ans_val, n.val)
            if n.left:
                st.append((n.left, max_ans_val, min_ans_val))
            if n.right:
                st.append((n.right, max_ans_val, min_ans_val))
        
        return max_v