class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = prices[0]
        profit = 0

        for price in prices:
            sell = min(sell, price)
            profit = max(profit, price-sell)

        return profit