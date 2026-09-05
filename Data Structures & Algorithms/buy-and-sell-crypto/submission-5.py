class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l == 1:
            return 0

        left = 0
        right = 1

        profit = 0

        while right < l:
            buy = prices[left]
            sell = prices[right]
            profit = max(profit, sell-buy)

            if sell < buy:
                left = right
                right += 1
            else:
                right += 1

        return profit

