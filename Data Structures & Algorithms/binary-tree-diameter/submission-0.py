# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        bestDiameter = 0
        if not root:
            return bestDiameter
        def findDepth(node):
            nonlocal bestDiameter
            if not node:
                return -1
            left = findDepth(node.left) + 1
            right = findDepth(node.right) + 1
            bestDiameter = max(left + right,bestDiameter)
            return max(left,right)
        heightOfTree = findDepth(root)
        return max(heightOfTree,bestDiameter)
        