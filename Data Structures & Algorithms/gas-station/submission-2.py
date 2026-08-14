class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        totalGas = totalCost = 0
        diff = []

        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]

            diff.append(gas[i] - cost[i])

        if totalGas < totalCost:
            return -1

        maxStep = [0, -math.inf]

        for i in range(len(diff)):
            if i == 0:
                step = diff[i] - diff[len(diff) - 1]
            else:
                step = diff[i] - diff[i - 1]

            if step > maxStep[1]:
                maxStep = [i, step]

        return maxStep[0]