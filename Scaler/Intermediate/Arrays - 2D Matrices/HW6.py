class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        sum = 0
        for i in range(n):
            for j in range(n):
                if i==j:
                    sum += A[i][j]
        return sum