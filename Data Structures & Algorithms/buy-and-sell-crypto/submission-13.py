class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maximum = 0

        for price in prices:
            lowest = min(price, lowest)
            maximum = max(price - lowest, maximum)

        return maximum