class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        def gcd(a, b):
            while b!=0:
                a, b = b, a%b
            return a
        
        gcd_prev = A[0]
        for n in A[1:]:
            gcd_prev = gcd(gcd_prev, n)
        return gcd_prev