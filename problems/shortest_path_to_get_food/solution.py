class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ans = -1
        r = len(grid)
        c = len(grid[0])
        
        def bfs(m, n):
            q = collections.deque()
            visited = set()
            dist = 1
            for p in ((m-1, n), (m+1, n), (m, n-1), (m, n+1)):
                if 0<=p[0]<r and 0<=p[1]<c:
                    q.append(p)
            while q:
                ql = len(q)
                for _ in range(ql):
                    i, j = q.popleft()
                    if (i, j) in visited:
                        continue
                    if grid[i][j] == '#':
                        return dist
                    elif grid[i][j] == 'O':
                        for p in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                            if 0<=p[0]<r and 0<=p[1]<c:
                                q.append(p)
                    visited.add((i,j))
                if len(visited) == r*c:
                    return -1
                dist += 1
            return -1
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '*':
                    ans = bfs(i, j)
                    break
        
        return ans