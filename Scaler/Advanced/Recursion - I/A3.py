class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if A == 0:
            return 0
        if B == 0:
            return 1
        p = self.pow(A%C, B//2, C) % C
        if B % 2 == 0:
            return (p*p) % C
        else:
            return (A%C * (p*p)%C ) % C