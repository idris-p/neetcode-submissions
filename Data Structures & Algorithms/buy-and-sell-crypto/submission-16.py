class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        result = 0

        for price in prices:
            lowest = min(lowest, price)
            result = max(price - lowest, result)

        return result