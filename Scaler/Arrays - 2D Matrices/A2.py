class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        ans = []
        j = 0
        while j < n:
            x, y = 0, j
            row = []
            while x < n and y >= 0:
                row.append(A[x][y])
                x += 1
                y -= 1
            z = len(row)
            while z <= n-1:
                row.append(0)
                z += 1
            ans.append(row)
            j += 1
        j = 1
        while j < n:
            x, y = j, n-1
            row = []
            while x < n and y >= 0:
                row.append(A[x][y])
                x += 1
                y -= 1
            z = len(row)
            while z <= n-1:
                row.append(0)
                z += 1
            ans.append(row)
            j += 1
        return ans