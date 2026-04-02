class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                maximum = max(profit, maximum)
        return maximum