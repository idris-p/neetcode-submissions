class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxProfit = 0

        for price in prices:
            if price > lowest:
                profit = price - lowest
                maxProfit = max(profit, maxProfit)
            lowest = min(price, lowest)

        return maxProfit