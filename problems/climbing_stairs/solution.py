class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [-1]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        
        def cs(n):
            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n]
        
        return dp[n] if n <= 2 else cs(n)