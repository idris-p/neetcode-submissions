# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root]) if root else []
        result = []

        while queue:
            currentLevelLength = len(queue)
            for i in range(currentLevelLength):
                current = queue.popleft()

                if i == currentLevelLength - 1:
                    result.append(current.val)
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return result