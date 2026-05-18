class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: set() for i in range(n)}

        for v1, v2 in edges:
            if v2 not in adjList[v1]:
                adjList[v1].add(v2)
            if v1 not in adjList[v2]:
                adjList[v2].add(v1)

        visited = set()
        edgesExplored = -1
        def dfs(node, prev):
            nonlocal edgesExplored

            edgesExplored += 1

            if node in visited:
                return False

            if len(adjList[node]) == 1 and edgesExplored == len(edges):
                visited.add(node)
                return True

            visited.add(node)

            result = True
            for neighbor in adjList[node]:
                if neighbor != prev:
                    result = result and dfs(neighbor, node)
                    if not result:
                        return False

            return True

        return dfs(0, None) and len(visited) == n