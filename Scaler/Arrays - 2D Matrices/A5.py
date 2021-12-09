class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(A[0])

        C = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(A[i][j] - B[i][j])
            C.append(row)
        return C
            