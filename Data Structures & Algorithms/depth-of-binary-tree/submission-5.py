# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        nodes = [[root, 1]]
        maximum = 0

        while nodes:
            node, level = nodes.pop()
            if node:
                maximum = max(level, maximum)
                nodes.append([node.left, 1 + level])
                nodes.append([node.right, 1 + level])
        return maximum