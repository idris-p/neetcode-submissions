class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {len(cost): 0} # i: minCost

        for i in range(len(cost) - 1, -1, -1):
            if i == len(cost) - 1:
                cache[i] = cost[i]
            else:
                cache[i] = min(cost[i] + cache[i+1], cost[i] + cache[i+2])

        return min(cache[0], cache[1])