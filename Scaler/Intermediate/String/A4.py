class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        return 1 if A == A[::-1] else 0