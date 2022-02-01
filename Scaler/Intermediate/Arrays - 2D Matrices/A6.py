class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        r = len(A)
        c = len(A[0])
        AT = []
        for i in range(c):
            row = []
            for j in range(r):
                row.append(A[j][i])
            AT.append(row)
        return AT