import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)

            residue = stone1 - stone2
            if residue > 0:
                heapq.heappush_max(stones, residue)

        if stones:
            return stones[0]
        return 0