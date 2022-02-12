import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if B == 0:
            return 1 if A != 0 else 0
        else:
            if B % 2 == 0:
                return self.pow((A*A)%C, B//2, C) % C
            else:
                return (A * self.pow((A*A)%C, (B-1)//2, C) % C )%C