class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.end = True

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = { len(s): 0 }
        trie = Trie(dictionary)
        
        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)

            curr = trie.root
            for j in range(i,len(s)):
                if s[j] in curr.children:
                    curr = curr.children[s[j]]
                    if curr.end == True:
                        res = min(res,dfs(j+1))
                else:
                    break
            
            dp[i] = res
            return res

        return dfs(0)