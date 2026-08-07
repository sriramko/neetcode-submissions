# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def findGood(subroot: TreeNode, biggestVal: int) -> int:
            if not subroot:
                return 0
            if subroot.val >= biggestVal:
                return 1 + findGood(subroot.left, subroot.val) + findGood(subroot.right, subroot.val)
            else:
                return findGood(subroot.left, biggestVal) + findGood(subroot.right, biggestVal)

        return findGood(root,root.val)
