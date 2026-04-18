# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [0, 0, True]

            left = dfs(node.left)
            right = dfs(node.right)

            leftDepth = 1 + max(left[0], left[1])
            rightDepth = 1 + max(right[0], right[1])
            balanced = left[2] and right[2]

            if abs(leftDepth - rightDepth) > 1:
                balanced = False

            return [leftDepth, rightDepth, balanced]

        return dfs(root)[2]