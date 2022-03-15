import math

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        return self.get_kth_magic_number(A, C, B)

    def lcm(self, a, b):
        return a*b//math.gcd(a, b)
    
    def get_kth_magic_number(self, A, B, C):
        # divisible by B - X//B
        # divisible by C - X//C
        # divisible by B and C - X//LCM(B, C)
        l, h = 1, A*min(B, C)
        while l < h:
            m = (l+h)//2
            if m//B + m//C - m//self.lcm(B, C) < A:
                l = m+1
            else:
                h = m
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.solve(14, 10, 12))
    print(s.solve(19, 11, 13))