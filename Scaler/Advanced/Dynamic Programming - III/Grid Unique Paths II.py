import functools
import sys
sys.setrecursionlimit(10**9)

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        m, n = len(A), len(A[0])
        @functools.lru_cache(None)
        def find_path(i, j):
            if i < 0 or j < 0 or A[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            return find_path(i-1, j) + find_path(i, j-1)
        
        return find_path(m-1, n-1) % (10 ** 9 + 7)