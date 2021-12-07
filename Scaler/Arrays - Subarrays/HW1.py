class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        c = 0
        for i in range(n):
            sub_sum = 0
            for j in range(i, n):
                sub_sum += A[j]
                if sub_sum < B:
                    c += 1
        return c