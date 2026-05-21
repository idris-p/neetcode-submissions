class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        path = set()
        connected = False
        size = 0
        def dfs(node, prev):
            nonlocal size
            nonlocal connected

            if node in path:
                return False
            if node in visited:
                return True

            visited.add(node)
            path.add(node)
            size += 1

            if size == n:
                connected = True

            for neighbor in graph[node]:
                if neighbor != prev:
                    result = dfs(neighbor, node)
                    if not result:
                        return False

            path.remove(node)
            return True

        for node in graph:
            if node not in visited:
                size = 0
                if not dfs(node, None):
                    return False

        return connected