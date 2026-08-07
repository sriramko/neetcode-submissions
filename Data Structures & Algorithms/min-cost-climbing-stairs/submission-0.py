class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mincost = [-1] * n
        mincost[n-1] = cost[n-1]
        mincost[n-2] = cost[n-2]
        if n > 2:
            for i in range(n-3,-1,-1):
                mincost[i] = cost[i] + min(mincost[i+1],mincost[i+2])
        return min(mincost[0],mincost[1])
