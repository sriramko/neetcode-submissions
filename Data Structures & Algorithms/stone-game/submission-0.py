class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {} #(l,r) -> how much current person can win from this position - the diff

        def dfs(l,r):
            if l == r:
                dp[(l,r)] = piles[l]
            if (l,r) in dp:
                return dp[(l,r)]
            dp[(l,r)] = max(piles[l] - dfs(l+1,r), piles[r] - dfs(l, r - 1))
            return dp[(l,r)]
        
        return dfs(0,len(piles) - 1) > 0
            
             
