class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, highestProfit = prices[0], 0

        for price in prices:
            highestProfit = max(price - lowest, highestProfit)
            lowest = min(price, lowest)
            
        return highestProfit