# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        #returns height
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            hl, hr = dfs(node.left), dfs(node.right)
            diameter = max(diameter, hl + hr)
            return 1 + max(hl,hr)
        dfs(root)
        return diameter