class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        sum = 0
        for i in range(n):
            for j in range(n):
                tc = (i+1)*(j+1)
                br = (n-i)*(n-j)
                sub = tc*br
                sum += sub*A[i][j]
        return sum