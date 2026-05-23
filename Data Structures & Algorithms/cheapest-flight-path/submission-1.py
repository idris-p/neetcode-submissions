class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [math.inf] * n
        graph[src] = 0

        temp = graph.copy()

        for i in range(k + 1):
            for source, dest, cost in flights:
                x = graph[source] + cost
                if x < temp[dest]:
                    temp[dest] = x
            graph = temp.copy()

        if graph[dst] == math.inf:
            return -1
        return graph[dst]