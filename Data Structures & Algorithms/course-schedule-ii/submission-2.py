from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        q = deque()

        adjList = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for crs, pre in prerequisites:
            adjList[pre].append(crs)
            indegrees[crs] += 1

        for crs in range(numCourses):
            if indegrees[crs] == 0:
                q.append(crs)

        while q:
            curr = q.popleft()
            res.append(curr)
            for adj in adjList[curr]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    q.append(adj)

        return res if len(res) == numCourses else []