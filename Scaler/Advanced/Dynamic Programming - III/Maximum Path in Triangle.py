import functools
import itertools
import sys
import math
sys.setrecursionlimit(10**9)

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        row = len(A)
        @functools.lru_cache(None)
        def max_total(r, c):
            if r >= row:
                return -math.inf
            if c >= len(A[r]):
                return -math.inf
            if r == row - 1:
                return A[r][c]
            return max(max_total(r+1, c), max_total(r+1, c+1)) + A[r][c]
        return max_total(0, 0)