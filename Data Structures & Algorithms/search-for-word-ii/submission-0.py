class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()

        for word in words:
            curr = self.root
            for letter in word:
                if letter not in curr.children:
                    curr.children[letter] = TrieNode()
                curr = curr.children[letter]
            curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        trie = Trie(words)
        res = set()
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        visit = set()

        def dfs(r,c,node,word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or board[r][c] not in node.children:
                return
            visit.add((r,c))

            child = node.children[board[r][c]]
            word += board[r][c]
            if child.isWord:
                res.add(word)
            
            for dr, dc in dirs:
                dfs(r+dr,c+dc, child, word)
            visit.remove((r,c))
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row,col,trie.root,"")

        return list(res)
