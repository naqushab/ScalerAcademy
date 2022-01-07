class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        pair_set = set(A)
        c = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                s = A[i]+A[j]
                if s in pair_set:
                    c += 1
        return c