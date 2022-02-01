class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        r = set()
        c = set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    r.add(i)
                    c.add(j)
        for i in r:
            for j in range(len(A[0])):
                A[i][j] = 0
        for i in c:
            for j in range(len(A)):
                A[j][i] = 0
        return A