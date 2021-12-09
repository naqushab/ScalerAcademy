class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        m = len(A)
        n = len(A[0])
        C = []
        for i in range(m):
            col = []
            for j in range(n):
                col.append(A[i][j] + B[i][j])
            C.append(col)
        return C