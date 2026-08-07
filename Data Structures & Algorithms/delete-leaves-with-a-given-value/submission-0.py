# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def delete(node) -> bool:
            if not node:
                return False
            if delete(node.left):
                node.left = None
            if delete(node.right):
                node.right = None
            if node.val == target and not node.left and not node.right:
                return True
        
        if delete(root):
            root = None
        return root
