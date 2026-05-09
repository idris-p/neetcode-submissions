import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max heap with k smallest elements
        closestPoints = []

        for point in points:
            distance = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            
            if len(closestPoints) < k:
                heapq.heappush_max(closestPoints, (distance, point))
            elif distance < closestPoints[0][0]:
                while len(closestPoints) >= k:
                    heapq.heappop_max(closestPoints)
                heapq.heappush_max(closestPoints, (distance, point))

        result = []
        for point in closestPoints:
            result.append(point[1])

        return result