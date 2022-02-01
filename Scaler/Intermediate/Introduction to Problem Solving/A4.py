import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        l, r = 0, A
        while l <= r:
            m = (l+r)//2
            if m*m == A:
                return m
            elif m*m > A:
                r = m-1
            else:
                l = m+1
        return -1