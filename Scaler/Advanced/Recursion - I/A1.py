class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0:
            return A
        return self.solve(A//10) + A%10