class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maximum = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maximum = max(profit, maximum)
            else:
                l = r
            r += 1
        return maximum