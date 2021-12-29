from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        q = deque()
        ans = [[float('+inf')]*c for _ in range(r)]
        
        def bfs(q):
            while q:
                ti, tj = q.popleft()
                for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = ti+d[0], tj+d[1]
                    if 0<=ni<r and 0<=nj<c:
                        if ans[ni][nj] > ans[ti][tj] + 1:
                            ans[ni][nj] = ans[ti][tj] + 1
                            q.append((ni, nj))
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i, j))
        bfs(q)
        return ans