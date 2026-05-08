# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, greatestSeen):
            if not node:
                return

            nonlocal result

            if node.val >= greatestSeen:
                result += 1
                greatestSeen = node.val
            
            dfs(node.left, greatestSeen)
            dfs(node.right, greatestSeen)

            return

        dfs(root, -math.inf)
        return result