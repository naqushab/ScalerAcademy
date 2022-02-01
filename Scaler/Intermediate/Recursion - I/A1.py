import sys
sys.setrecursionlimit(5*(10**4))

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        def check_pal(A, s, e):
            if s >= e:
                return 1
            if A[s] != A[e]:
                return 0
            else:
                return check_pal(A, s+1, e-1)
        return check_pal(A, 0, len(A)-1)