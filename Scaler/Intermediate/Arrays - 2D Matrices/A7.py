class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for i in range(n):
            for j in range(n//2):
                A[i][j], A[i][n-1-j] = A[i][n-1-j], A[i][j]
        return A