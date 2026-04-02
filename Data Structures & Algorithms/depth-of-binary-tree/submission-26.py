# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.current, self.maximum = 0, 0

        def traverse(node):
            if not node:
                return

            self.current += 1
            self.maximum = max(self.current, self.maximum)

            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            
            self.current -= 1

        traverse(root)

        return self.maximum