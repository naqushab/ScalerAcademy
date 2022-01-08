class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        dp = [[[-1 for _ in range(c+1)] for _ in range(c+1) ] for _ in range(r+1)]
        
        def dfs(rc, c1, c2):
            r = len(grid)
            c = len(grid[0])
            if rc == r:
                return 0
            
            if dp[rc][c1][c2] != -1:
                return dp[rc][c1][c2]
            
            if c1 == c2:
                cur_cost = grid[rc][c1]
            else:
                cur_cost = grid[rc][c1] + grid[rc][c2]
            
            ans = 0
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    nc1 = c1+i
                    nc2 = c2+j
                    if 0 <= nc1 < c and 0<=nc2<c:
                        ans = max(ans, cur_cost+dfs(rc+1, nc1, nc2))
            
            dp[rc][c1][c2] = ans
            return dp[rc][c1][c2]
        
        return dfs(0, 0, c-1)