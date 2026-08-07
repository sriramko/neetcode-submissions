# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered = []
        
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            ordered.append(node.val)
            print(node.val)
            inOrder(node.right)
        
        inOrder(root)
        print(ordered)
        return ordered[k-1]
