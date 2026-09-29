class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []
        def backtrack(start):
            if len(comb) == k:
                res.append(comb.copy())
                return
            if start == n + 1:
                return
            comb.append(start)
            backtrack(start + 1)
            comb.pop()
            backtrack(start + 1)
        
        backtrack(1)
        return res