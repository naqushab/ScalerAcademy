class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = math.inf
        for stock_val in prices:
            min_price = min(min_price, stock_val)
            max_profit = max(max_profit, stock_val - min_price)
        return max_profit