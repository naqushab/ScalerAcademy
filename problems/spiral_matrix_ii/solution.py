class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        g = [ [0]*n for _ in range(n) ]
        sq = n*n
        i = 1
        r, d, l, u = True, False, False, False
        row, col = 0, 0
        while i <= sq:
            if r:
                while 0 <= row < n and 0 <= col < n and g[row][col] == 0:
                    g[row][col] = i
                    col += 1
                    i += 1
                r, d = False, True
                row += 1
                col -= 1
            if d:
                while 0 <= row < n and 0 <= col < n and g[row][col] == 0:
                    g[row][col] = i
                    row += 1
                    i += 1
                d, l = False, True
                col -= 1
                row -= 1
            if l:
                while 0 <= row < n and 0 <= col < n and g[row][col] == 0:
                    g[row][col] = i
                    col -= 1
                    i += 1
                l, u = False, True
                row -= 1
                col += 1
            if u:
                while 0 <= row < n and 0 <= col < n and g[row][col] == 0:
                    g[row][col] = i
                    row -= 1
                    i += 1
                u, r = False, True
                col += 1
                row += 1
        return g