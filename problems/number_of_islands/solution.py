class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        
        def mark_ones(m, n):
            if 0 <= m < r and 0 <= n < c and grid[m][n] == '1':
                grid[m][n] = '-1'
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_m, new_n = m + x, n + y
                    mark_ones(new_m, new_n)
            return

        count = 0
        for i, j in itertools.product(range(r), range(c)):
            if grid[i][j] == '1':
                count += 1
                mark_ones(i, j)
        
        return count