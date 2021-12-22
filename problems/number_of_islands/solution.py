class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                r = len(grid)
                c = len(grid[0])
                if 0<=i-1<=r-1 and 0<=j<=c-1:
                    dfs(grid, i-1, j)
                if 0<=i+1<=r-1 and 0<=j<=c-1:
                    dfs(grid, i+1, j)
                if 0<=i<=r-1 and 0<=j-1<=c-1:
                    dfs(grid, i, j-1)
                if 0<=i<=r-1 and 0<=j+1<=c-1:
                    dfs(grid, i, j+1)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(grid, i, j)
        return ans