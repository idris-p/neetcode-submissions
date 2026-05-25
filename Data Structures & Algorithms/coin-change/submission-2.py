class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [[None for i in range(amount + 1)] for j in range(len(coins))]
        coins.sort()

        def dfs(index, total, numCoins):
            if cache[index][total]:
                return cache[index][total]

            if total == amount:
                return numCoins
            if total > amount or index == -1:
                return math.inf

            result = math.inf
            count = (amount - total) // coins[index]
            for i in range(count, -1, -1):
                result = min(dfs(index - 1, total + i * coins[index], numCoins + i), result)

            cache[index][total] = result

            return result

        result = dfs(len(coins) - 1, 0, 0)
        return result if result != math.inf else -1