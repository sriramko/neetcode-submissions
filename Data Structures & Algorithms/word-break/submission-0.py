class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [False] * size
        dp.append(True) # bottom case
        for i in range(size-1, -1, -1):
            for word in wordDict:
                if s[i:i+len(word)] == word and dp[i+len(word)]:
                    dp[i] = True
                    break
        return dp[0]        
                