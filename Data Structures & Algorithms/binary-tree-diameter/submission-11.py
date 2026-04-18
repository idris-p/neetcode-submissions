# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            leftDepth = 1 + max(left[0], left[1])
            rightDepth = 1 + max(right[0], right[1])

            self.diameter = max(leftDepth + rightDepth, self.diameter)

            return [leftDepth, rightDepth]

        dfs(root)
        return self.diameter - 2