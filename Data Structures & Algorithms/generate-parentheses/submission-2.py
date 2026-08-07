class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        
        pars = self.generateParenthesis(n-1)
        res = set()
        for p in pars:
            for i in range(len(p)):
                res.add(p[:i] + "()" + p[i:])
        
        return list(res)