# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, bounds):
            if not node:
                return True

            left, right = True, True
            if node.left:
                left = dfs(node.left, [bounds[0], node.val - 1])
            if node.right:
                right = dfs(node.right, [node.val + 1, bounds[1]])

            return bounds[0] <= node.val <= bounds[1] and left and right
        
        return dfs(root, [-math.inf, math.inf])