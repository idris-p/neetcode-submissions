# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        depth = 0

        while stack:
            node, level = stack.pop()
            if node:
                stack.append([node.left, 1 + level])
                stack.append([node.right, 1 + level])
                depth = max(level, depth)
        return depth