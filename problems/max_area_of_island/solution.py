class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        def dfs(i, j):
            if 0 > i or i >= r or 0 > j or j >= c:
                return 0
            if grid[i][j] == 0:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 0
            return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1) 
        
        area = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    local_area = dfs(i, j)
                    area = max(area, local_area)
        return area