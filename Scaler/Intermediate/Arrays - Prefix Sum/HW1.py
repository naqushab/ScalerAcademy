class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        t = 0
        m = max(A)
        for n in A:
            t += m-n
        return t