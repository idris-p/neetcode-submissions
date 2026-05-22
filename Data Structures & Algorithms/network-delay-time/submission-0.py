import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {i: [] for i in range(n + 1)}
        del graph[0]

        for u, v, t in times:
            graph[u].append((v, t))

        minHeap = [(0, k)]
        visited = set()
        maxTime = 0

        while len(visited) < n:
            if not minHeap:
                return -1
                
            path, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            maxTime = max(path, maxTime)

            for neighbor, time in graph[node]:
                heapq.heappush(minHeap, (path + time, neighbor))

            visited.add(node)

        return maxTime