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

        head = copy = Node(node.val)
        # Hash map maps values to nodes
        valToNode = {node.val: copy}

        visited = set()
        def dfs(node):
            nonlocal copy

            if node in visited:
                return

            # Visit
            visited.add(node)
            for neighbor in node.neighbors:
                if neighbor.val not in valToNode:
                    valToNode[neighbor.val] = Node(neighbor.val)
                copy.neighbors.append(valToNode[neighbor.val])
            
            for neighbor in node.neighbors:
                copy = valToNode[neighbor.val]
                dfs(neighbor)

        dfs(node)
        return head