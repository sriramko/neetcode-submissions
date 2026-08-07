class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])
        length = numRows * numCols
        l = 0
        r = length - 1
        m = (l + r) // 2
        while l <= r:
            x = int(m % numCols)
            y = int(m / numCols)
            curr = matrix[y][x]
            if curr == target:
                return True
            elif target > curr:
                l = m + 1
            else:
                r = m - 1
            m = (l + r) // 2
        return False
            