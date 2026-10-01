class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjMap = defaultdict(list)
        for (v1, v2), val in zip(equations, values):
            adjMap[v1].append((v2, val))
            adjMap[v2].append((v1, 1 / val))

        def dfs(src, dst, visited):
            if src == dst:
                return 1.0
            visited.add(src)
            for nei, weight in adjMap[src]:
                if nei in visited:
                    continue
                res = dfs(nei, dst, visited)
                if res != -1:
                    return weight * res
            return -1.0

        res = []
        for q1, q2 in queries:
            if q1 not in adjMap or q2 not in adjMap:
                res.append(-1.0)
            else:
                res.append(dfs(q1, q2, set()))
        return res
        for q1, q2 in queries:
            res.append(calcDFS(q1,q2,"0"))
        return res