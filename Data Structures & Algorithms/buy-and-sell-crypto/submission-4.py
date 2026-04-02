class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if len(prices) == 1:
            return maxProfit

        l, r = 0, 1
        while r < len(prices):
            print(l, r)
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1

        return maxProfit