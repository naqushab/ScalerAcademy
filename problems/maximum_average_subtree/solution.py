# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        max_avg = [float('-inf')]
        
        def calc_avg(root, max_avg):
            if not root:
                return (0, 0)
            l = calc_avg(root.left, max_avg)
            r = calc_avg(root.right, max_avg)
            max_avg[0] = max(max_avg[0], (l[0]+r[0]+root.val)/(l[1]+r[1]+1))
            return (l[0]+r[0]+root.val), (l[1]+r[1]+1)
            
        calc_avg(root, max_avg)
        return max_avg[0]