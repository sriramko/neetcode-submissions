class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()

        def addCell(row, col):
            if (row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] <= 0 or (row, col) in visited):
                return
            q.append([row, col])
            visited.add((row, col))
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        dist = 0
        while q:
            batch = len(q)
            for i in range(batch):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            dist += 1 