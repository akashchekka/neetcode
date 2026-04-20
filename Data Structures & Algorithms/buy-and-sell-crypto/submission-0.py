class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = float('inf')
        profit = 0

        for i in prices:
            buyPrice = min(buyPrice, i)
            profit = max(profit, i - buyPrice)

        return profit