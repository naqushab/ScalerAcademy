class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        lm = float('+inf')
        for i in range(len(prices)):
            lm = min(lm, prices[i])
            p = max(p, prices[i]-lm)
        return p