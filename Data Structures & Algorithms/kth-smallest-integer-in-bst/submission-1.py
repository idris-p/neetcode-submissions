# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            if not node:
                return []

            seen = []
            if node.left:
                seen = dfs(node.left)
            seen += [node.val]
            if node.right and len(seen) < k:
                seen += dfs(node.right)

            return seen

        return dfs(root)[k-1]