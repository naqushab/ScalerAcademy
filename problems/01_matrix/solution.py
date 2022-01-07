class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        ans = [[math.inf]*c for _ in range(r)]
        q = collections.deque()
        
        def bfs(q):
            while q:
                ql = len(q)
                for _ in range(ql):
                    x, y = q.popleft()
                    for p in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                        m, n = p[0], p[1]
                        if 0<=m<r and 0<=n<c and ans[m][n] == math.inf:
                            ans[m][n] = ans[x][y]+1
                            q.append((m, n))
        
        for i, j in product(range(r), range(c)):
            if mat[i][j] == 0:
                ans[i][j] = 0
                q.append((i, j))
        
        bfs(q)
        
        return ans