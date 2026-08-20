class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(curr, par):
            time = 0
            for child in adj[curr]:
                if child == par:
                    continue
                childTime = dfs(child, curr)
                if childTime or hasApple[child]:
                    time += childTime + 2
            return time
        
        return dfs(0,-1)