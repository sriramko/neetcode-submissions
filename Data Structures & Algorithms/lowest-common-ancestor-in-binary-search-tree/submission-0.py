# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            temp = p
            p = q
            q = temp
        lower_bound = root.val < p.val
        upper_bound = root.val > q.val
        while upper_bound or lower_bound:
            if upper_bound:
                root = root.left
            else:
                root = root.right
            lower_bound = root.val < p.val
            upper_bound = root.val > q.val
        return root