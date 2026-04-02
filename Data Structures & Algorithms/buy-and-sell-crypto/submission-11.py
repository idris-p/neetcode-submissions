class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        lowest = prices[0]

        for price in prices:
            lowest = min(price, lowest)
            profit = price - lowest
            maximum = max(profit, maximum)

        return maximum