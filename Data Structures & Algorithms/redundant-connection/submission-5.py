class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [n for n in range(len(edges) + 1)]

        def find(node):
            if parent[node] != node:
                return find(parent[node])
            return node

        def union(x, y):
            groupX, groupY = find(x), find(y)
            if groupX != groupY:
                parent[find(y)] = parent[x]
                return True
            return False

        for a, b in edges:
            joined = union(a, b)
            if not joined:
                return [a, b]