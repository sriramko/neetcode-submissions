# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(greatest: int, node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            res = 0
            if node.val >= greatest:
                res += 1
                greatest = node.val
            return res + dfs(greatest, node.left) + dfs(greatest, node.right)
        return dfs(-101, root)