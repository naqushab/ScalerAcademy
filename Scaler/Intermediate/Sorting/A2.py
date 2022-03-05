class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) < 2:
            return 1
        A.sort()
        d = A[1] - A[0]
        for i in range(len(A)-1):
            if A[i+1] - A[i] != d:
                return 0
        return 1