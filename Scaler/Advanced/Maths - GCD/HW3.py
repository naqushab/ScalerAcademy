class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)
    
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        gcd = self.gcd(B, C)
        lcm = (B*C)//gcd
        count = 0
        for i in range(lcm, A+1, lcm):
            count += 1
        return count