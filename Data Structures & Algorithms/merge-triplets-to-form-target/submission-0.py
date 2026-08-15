class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        allowedTriplets = []
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                allowedTriplets.append([a, b, c])

        seen = [False, False, False]

        for a, b, c in allowedTriplets:
            if a == target[0]:
                seen[0] = True
            if b == target[1]:
                seen[1] = True
            if c == target[2]:
                seen[2] = True

        return seen[0] and seen[1] and seen[2]