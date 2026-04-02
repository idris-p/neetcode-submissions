class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        lowest = prices[0]

        for price in prices:
            lowest = min(price, lowest)
            maximum = max(price - lowest, maximum)

        return maximum