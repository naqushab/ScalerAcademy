from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        q = deque()
        
        def bfs(q):
            t = 0
            while q:
                ql = len(q)
                change = False
                for _ in range(ql):
                    ti, tj = q.popleft()
                    if grid[ti][tj] == 1:
                        change = True
                        grid[ti][tj] = 3
                    if 0 <= ti-1 < r and grid[ti-1][tj] == 1:
                        q.append((ti-1, tj))
                    if 0 <= ti+1 < r and grid[ti+1][tj] == 1:
                        q.append((ti+1, tj))
                    if 0 <= tj-1 < c and grid[ti][tj-1] == 1:
                        q.append((ti, tj-1))
                    if 0 <= tj+1 < c and grid[ti][tj+1] == 1:
                        q.append((ti, tj+1))
                if change:
                    t += 1
            return t
        
        def np():
            for i in range(r):
                for j in range(c):
                    if grid[i][j] == 1:
                        return True
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i, j))
        if not q:
            if np():
                return -1
            else:
                return 0
        
        ans = bfs(q)
        
        if np():
            return -1
        
        return ans