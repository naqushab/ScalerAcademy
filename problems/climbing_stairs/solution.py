class Solution:
    def soln1(self, n):
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
    
    @functools.lru_cache(None)
    def soln2(self, n):
        if n <= 2:
            return n
        return self.soln2(n-1) + self.soln2(n-2)
    
    def soln3(self, n):
        a, b = 0, 1
        for i in range(n+1):
            a, b = b, a+b
        return a
    
    def climbStairs(self, n: int) -> int:
        return self.soln3(n)