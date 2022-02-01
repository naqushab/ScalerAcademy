class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        m = len(A)
        n = len(A[0])
        if len(B) != n:
            return [[]]
        p = len(B[0])
        ans = []
        for i in range(m):
            row = []
            for j in range(p):
                t = 0
                for k in range(n):
                    t += A[i][k] * B[k][j]
                row.append(t)
            ans.append(row)
        return ans