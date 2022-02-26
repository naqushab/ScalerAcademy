class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0 or A == 1:
            return 1
        return A * self.solve(A-1)