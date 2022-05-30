import functools
import itertools
import sys
import math
sys.setrecursionlimit(10**9)

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        row = len(A)
        @functools.lru_cache(None)
        def min_total(r, c):
            if r >= row:
                return math.inf
            if c >= len(A[r]):
                return math.inf
            if r == row - 1:
                return A[r][c]
            return min(min_total(r+1, c), min_total(r+1, c+1)) + A[r][c]
        return min_total(0, 0)