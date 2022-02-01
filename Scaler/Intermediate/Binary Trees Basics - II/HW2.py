# Definition for a  binary tree node

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        self.ans = []
        if not A:
            return self.ans

        def dfs(root, x, temp):
            temp = temp + [root.val]
            
            if len(temp) > 0 and temp[-1] == x:
                self.ans = temp[:]
                return
            if root.left:
                dfs(root.left, x, temp)
            if root.right:
                dfs(root.right, x, temp)
        

        dfs(A, B, [])
        return self.ans

if __name__ == "__main__":
    s = Solution()
    # 15 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1 
    # 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    s.solve(A=root, B=4)
