class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        ans = [[0]*n for _ in range(n)]

        def recurse(x, y):
            if x == n-1 and y == n-1:
                ans[x][y] = 1
                return True
            if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                ans[x][y] = 1
                if recurse(x+1, y):
                    return True
                if recurse(x, y+1):
                    return True
                if recurse(x, y-1):
                    return True
                ans[x][y] = 0

        recurse(0, 0)
        return ans