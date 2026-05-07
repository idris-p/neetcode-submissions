# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node, target):
            if not node:
                return []
            if node.val == target:
                return [node]

            left, right = None, None
            if node.left:
                left = dfs(node.left, target)
            if node.right:
                right = dfs(node.right, target)

            if left:
                return left + [node]
            if right:
                return right + [node]

        pAncestors = dfs(root, p.val)
        qAncestors = dfs(root, q.val)

        pPointer, qPointer = 0, 0
        seen = set()

        while pPointer < len(pAncestors) or qPointer < len(qAncestors):
            if pPointer < len(pAncestors):
                if pAncestors[pPointer] in seen:
                    return pAncestors[pPointer]
                seen.add(pAncestors[pPointer])
                pPointer += 1

            if qPointer < len(qAncestors):
                if qAncestors[qPointer] in seen:
                    return qAncestors[qPointer]
                seen.add(qAncestors[qPointer])
                qPointer += 1