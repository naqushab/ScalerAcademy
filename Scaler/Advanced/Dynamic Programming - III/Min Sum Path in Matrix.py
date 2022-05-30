import sys
sys.setrecursionlimit(10**9)
import functools
import itertools

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        m, n = len(A), len(A[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(n):
            if i == 0:
                dp[0][i] = A[0][i]
            else:
                dp[0][i] = dp[0][i-1] + A[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + A[i][0]
        
        for i, j in itertools.product(range(1, m), range(1, n)):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + A[i][j]
        
        return dp[m-1][n-1]
    
    def top_down(self, A):
        @functools.lru_cache(None)
        def min_sum(i, j):
            if i < 0 or j < 0:
                return float('inf')
            if i == 0 and j == 0:
                return A[0][0]
            return min(min_sum(i-1, j), min_sum(i, j-1)) + A[i][j]
        m, n = len(A), len(A[0])
        return min_sum(m-1, n-1)