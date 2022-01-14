class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def bottom_up():
            dp = [amount+1]*(amount+1)
            dp[0] = 0

            for a in range(1, amount+1):
                for c in coins:
                    if a - c >= 0:
                        dp[a] = min(dp[a], 1+dp[a-c])

            return dp[amount] if dp[amount] != amount+1 else -1
        
        def top_down():
            if not amount:
                return 0
            q = collections.deque()
            ans = 0
            q.append((0, 0))
            visited = [True] + [False]*amount
            while q:
                ql = len(q)
                for _ in range(ql):
                    a, ans = q.popleft()
                    if a == amount:
                        return ans
                    for c in coins:
                        if a+c <= amount and not visited[a+c]:
                            visited[a+c] = True
                            q.append((a+c, ans+1))
                            
            return -1
        
        return top_down()