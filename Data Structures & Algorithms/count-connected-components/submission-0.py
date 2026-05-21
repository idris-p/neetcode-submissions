class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        total = 0

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor != prev:
                    dfs(neighbor, node)

        for node in graph:
            if node not in visited:
                total += 1
                dfs(node, None)

        return total