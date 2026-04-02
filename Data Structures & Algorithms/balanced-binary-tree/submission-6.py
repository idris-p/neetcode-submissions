# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.imbalanceFound = False
        
        def height(node):
            if not node:
                return [0, 0]

            leftHeights = height(node.left)
            rightHeights = height(node.right)

            left = max(leftHeights[0], leftHeights[1]) + 1
            right = max(rightHeights[0], rightHeights[1]) + 1

            if abs(left - right) > 1:
                self.imbalanceFound = True
            
            return [left, right]

        result = height(root)

        return abs(result[0] - result[1]) <= 1 and not self.imbalanceFound