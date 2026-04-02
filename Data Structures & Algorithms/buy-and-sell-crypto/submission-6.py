class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] - prices[l] > 0:
                profit = prices[r] - prices[l]
                maximum = max(profit, maximum)
            else:
                l = r
            r += 1

        return maximum