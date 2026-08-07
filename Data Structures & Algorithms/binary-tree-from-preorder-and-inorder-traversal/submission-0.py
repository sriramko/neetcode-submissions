# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def split(inorder, preorder):
            if not preorder or not inorder:
                return None
            node = TreeNode(val=preorder[0])

            idx = inorder.index(node.val)
            leftin = inorder[:idx]
            leftpre = preorder[1:1+len(leftin)]
            rightin = inorder[1+len(leftin):]
            rightpre = preorder[len(leftin)+1:]
            node.left = split(leftin,leftpre)
            node.right = split(rightin,rightpre)
            return node
        
        return split(inorder, preorder)
        

