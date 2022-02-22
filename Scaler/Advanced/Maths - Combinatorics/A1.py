class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        # pascal's triangle
        B = min(B, A-B)
        pascal = [0]*(A+1)
        pascal[0] = 1
        for i in range(1, A+1):
            for j in range(min(i, B), 0, -1):
                pascal[j] += pascal[j-1]
                pascal[j] %= C
        return pascal[B] % C