# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def maxDepthLR(node):
            if not node:
                return [0, 0]

            maxL, maxR = 0, 0
            if node.left:
                stack = [[node.left, 1]]

                while stack:
                    current, depth = stack.pop()

                    maxL = max(depth, maxL)

                    if current.left:
                        stack.append([current.left, depth + 1])
                    if current.right:
                        stack.append([current.right, depth + 1])

            if node.right:
                stack = [[node.right, 1]]

                while stack:
                    current, depth = stack.pop()

                    maxR = max(depth, maxR)

                    if current.left:
                        stack.append([current.left, depth + 1])
                    if current.right:
                        stack.append([current.right, depth + 1])

            return [maxL, maxR]

        if not root:
            return 0

        stack = [root]
        diameter = 0

        while stack:
            node = stack.pop()

            l, r = maxDepthLR(node)
            diameter = max(l + r, diameter)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return diameter