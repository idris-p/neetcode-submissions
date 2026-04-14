class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0, *cost, 0]

        def dp(cost, cache={}):
            if len(cost) == 1 or len(cost) == 2:
                return 0
            if str(cost) in cache:
                return cache[str(cost)]

            oneStep = cost[1] + dp(cost[1:], cache)
            twoStep = cost[2] + dp(cost[2:], cache)

            result = min(oneStep, twoStep)
            cache[str(cost)] = result

            return result

        return dp(cost)