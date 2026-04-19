class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = cost + [0]
        table = [0] * (len(cost))
        table[0] = cost[0]
        table[1] = cost[1]

        for i in range(2, len(cost)):
            table[i] = min(table[i - 1], table[i - 2]) + cost[i]

        return table[len(cost) - 1]