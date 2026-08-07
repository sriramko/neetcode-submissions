class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sums = matrix
        n = len(matrix[0])
        m = len(matrix)
        for row in range(0,m):
            for col in range(0,n):
                if row != 0:
                    self.sums[row][col] += self.sums[row - 1][col]
                if col != 0:
                    self.sums[row][col] += self.sums[row][col - 1]
                if row != 0 and col != 0:
                    self.sums[row][col] -= self.sums[row - 1][col - 1]
        print(self.sums)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret = self.sums[row2][col2] 
        if row1 != 0:
            ret -= self.sums[row1 - 1][col2]
        if col1 != 0:
            ret -= self.sums[row2][col1 - 1]
        if row1 != 0 and col1 != 0:
            ret += self.sums[row1 - 1][col1 - 1]
        return ret


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)