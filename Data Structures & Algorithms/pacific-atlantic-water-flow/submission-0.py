class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r,c,visit,prevHeight):
            if (r,c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0,c,pacific, heights[0][c])
            dfs(ROWS-1,c, atlantic, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r,0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS-1])
        both = [[i,j] for (i,j) in (atlantic & pacific)]
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if (i,j) in pacific and (i,j) in atlantic:
        #             both.append([i,j])
        
        return both
