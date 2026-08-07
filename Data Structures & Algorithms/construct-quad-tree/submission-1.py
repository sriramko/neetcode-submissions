"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(grid) == 1:
            res = Node()
            res.val = bool(grid[0][0])
            res.isLeaf = True
            return res
        N = len(grid)
        res = Node()
        gridTL = [grid[i][0:N//2] for i in range(N//2)]
        gridTR = [grid[i][N//2:N] for i in range(N//2)]
        gridBL = [grid[i][0:N//2] for i in range(N//2,N)]
        gridBR = [grid[i][N//2:N] for i in range(N//2,N)]
        topLeft = self.construct(gridTL)
        topRight = self.construct(gridTR)
        bottomLeft = self.construct(gridBL)
        bottomRight = self.construct(gridBR)
        if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf
            and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            res.isLeaf = True
            res.val = topLeft.val
        else:
            res.isLeaf = False
            res.val = True
            res.topLeft = topLeft
            res.topRight = topRight
            res.bottomLeft = bottomLeft
            res.bottomRight = bottomRight
        return res
