class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = math.inf
        maxK = 0
        for pile in piles:
            maxK = max(pile, maxK)

        l, r = 1, maxK
        while l <= r:
            k = l + (r - l) // 2

            hoursTaken = 0
            for pile in piles:
                remainder = pile % k
                if remainder == 0:
                    hoursTaken += pile // k
                else:
                    hoursTaken += pile // k + 1

            if hoursTaken > h:
                l = k + 1
            else:
                result = min(k, result)
                r = k - 1

        return result