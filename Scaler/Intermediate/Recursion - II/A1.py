class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        hp = pow(A, B//2, C)%C
        if A == 0:
            return 0
        if B == 0:
            return 1
        if B%2 == 0:
            return (hp*hp)%C
        else:
            return ((A%C)*((hp*hp)%C))%C