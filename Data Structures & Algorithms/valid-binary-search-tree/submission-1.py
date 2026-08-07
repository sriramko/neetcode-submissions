# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validRec(subroot, lower, upper) -> bool:
            if not subroot:
                return True
            if subroot.val > lower and subroot.val < upper:
                return validRec(subroot.left, lower, subroot.val) and validRec(subroot.right, subroot.val, upper)
            else:
                return False

        return validRec(root, float("-inf"), float("inf"))