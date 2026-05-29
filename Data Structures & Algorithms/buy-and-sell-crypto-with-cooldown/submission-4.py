class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {n: [None, None] for n in range(len(prices))}

        def dfs(day, buying):
            if day >= len(prices):
                return 0
            val = 1 if buying else 0
            if cache[day][val] != None:
                return cache[day][val]

            cooldown = dfs(day + 1, buying)
            if buying:
                buy = dfs(day + 1, not buying) - prices[day]
                cache[day][1] = max(cooldown, buy)
                return cache[day][1]
            else:
                sell = dfs(day + 2, not buying) + prices[day]
                cache[day][0] = max(cooldown, sell)
                return cache[day][0]

        return dfs(0, True)