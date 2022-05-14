class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        r, c = len(grid), len(grid[0])
        q = collections.deque()
        
        def rot_orange():
            time = 0
            while q:
                ql = len(q)
                rotted = False
                for _ in range(ql):
                    m, n = q.popleft()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        x, y = m + dx, n + dy
                        if 0 <= x < r and 0 <= y < c and grid[x][y] == 1 and (x, y) not in visited:
                            rotted = True
                            visited.add((x, y))
                            grid[x][y] = 2
                            q.append((x, y))
                if rotted:
                    time += 1
            return time
                            
        
        for i, j in itertools.product(range(r), range(c)):
            if grid[i][j] == 2:
                q.append((i, j))
        
        time = rot_orange()
        
        for i, j in itertools.product(range(r), range(c)):
            if grid[i][j] == 1:
                return -1
            
        return time