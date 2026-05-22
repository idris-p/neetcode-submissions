import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = {n: [] for n in range(len(points))}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                manhattan = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                graph[i].append((j, manhattan))
                graph[j].append((i, manhattan))

        minHeap = [(0, 0)]
        visited = set()
        result = 0

        while len(visited) < len(points):
            cost, point = heapq.heappop(minHeap)

            if point in visited:
                continue

            result += cost

            for neighbor, distance in graph[point]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (distance, neighbor))
            
            visited.add(point)

        return result