class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adjList = [[] for _ in range(n)]
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visited = set()
        def dfs(node: int, par: int) -> bool:
            if node in visited:
                return False

            visited.add(node)
            for adj in adjList[node]:
                if adj == par:
                    continue
                if not dfs(adj, node):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n
