class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])

        def backtrack(x,y,word):
            if len(word) == 0:
                return True
            if y < 0 or y >= height or x < 0 or x >= width:
                return False
            if board[y][x] != word[0]:
                return False
            curr = board[y][x]
            board[y][x] = "#"
            remainder = word[1:]
            found = backtrack(x+1,y,remainder) or backtrack(x-1,y,remainder) or backtrack(x,y+1,remainder) or backtrack(x,y-1,remainder)
            board[y][x] = curr
            return found

        for r in range(height):
            for c in range(width):
                if backtrack(c,r,word):
                    return True
        return False