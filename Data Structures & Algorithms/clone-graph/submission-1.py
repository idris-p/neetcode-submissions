"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        copy = Node(node.val)

        # Hash map
        oldToNew = {node: copy}

        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            
            for neighbor in node.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                oldToNew[node].neighbors.append(oldToNew[neighbor])
                dfs(neighbor)

        dfs(node)
        return copy