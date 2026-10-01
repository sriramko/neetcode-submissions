# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #returns height
        def dfs(node):
            if not node:
                return [0,0]
            h1, d1 = dfs(node.left)
            h2, d2 = dfs(node.right)
            diameter = max(h1 + h2, d1, d2)
            return [1 + max(h1,h2), diameter]
        return dfs(root)[1]