import sys
sys.setrecursionlimit(1000000)

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if B < 0:
            return A
        if B == 0:
            return 1 if A != 0 else 0
        else:
            if B % 2 == 0:
                return self.pow((A*A)%C, B//2, C) % C
            else:
                return (A * self.pow((A*A)%C, (B-1)//2, C) % C )%C

    def solve(self, A, B, C):
        B = min(B, A-B)
        numerator = 1
        denominator = 1
        for i in range(B):
            numerator = (numerator * (A-i)) % C
            denominator = (denominator * (i+1)) % C
        return (numerator % C * self.pow(denominator, C-2, C) % C) % C