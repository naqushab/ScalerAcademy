class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A < 10:
            return 1 if A == 1 else 0
        return self.solve(self.sum_digit(A))
    
    def sum_digit(self, A):
        if A == 0:
            return A
        return self.sum_digit(A//10) + A%10