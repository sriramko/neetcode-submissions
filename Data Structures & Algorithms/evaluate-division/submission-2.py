class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjMap = defaultdict(list)
        for (v1, v2), val in zip(equations,values):
            adjMap[v1].append([v2, val])
            adjMap[v2].append([v1, (1 / val)])
        
        def calcDFS(var1, var2, varprev): #varprev prevents back and forth forever
            for varx, value in adjMap[var1]:
                if varx == varprev:
                    continue
                if var1 == var2:
                    return 1
                if varx == var2:
                    return value
                else:
                    res = calcDFS(varx,var2,var1)
                    if res != -1:
                        return value * res
            return -1

        res = []
        for q1, q2 in queries:
            res.append(calcDFS(q1,q2,"0"))
        return res