class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = { i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist,j))
                adj[j].append((dist,i))

        # Prim's
        res = 0
        visit = set()
        minH = [[0,0]] # cost, point index
        heapq.heapify(minH)
        while len(visit) < N:
            dist, point = heapq.heappop(minH)
            if point in visit:
                continue
            res += dist
            visit.add(point)
            for neiCost, nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res