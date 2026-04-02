# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False

            return tree1.val == tree2.val and isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)

        self.subtreeFound = False
        
        def dfs(root):
            if isSameTree(root, subRoot):
                self.subtreeFound = True

            if root:
                dfs(root.left)
                dfs(root.right)

            return

        dfs(root)

        return self.subtreeFound
