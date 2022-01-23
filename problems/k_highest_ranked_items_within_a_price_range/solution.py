class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        ans = []
        q = collections.deque()
        m, n = len(grid), len(grid[0])
        r, c = start
        q.append((0, grid[r][c], r, c))
        seen = set()
        seen.add((r, c))
        
        while q:
            dist, cost, r, c = q.popleft()
            if pricing[0] <= cost <= pricing[1]:
                ans += [[ dist, cost, r, c ]]
            for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
                x = r + i
                y = c + j
                if 0<=x<m and 0<=y<n and (x,y) not in seen and grid[x][y] != 0:
                    q.append((1+dist, grid[x][y], x, y))
                    seen.add((x,y))
        
        ans.sort()
        return [[x, y] for _, _, x, y in ans[:k]]