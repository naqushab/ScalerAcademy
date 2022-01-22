class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        for i in range(1, math.floor(math.sqrt(n))+1):
            if not self.winnerSquareGame(n-i*i):
                return True
        return False