class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i, (px, py) in enumerate(points):
            dist = px**2 + py**2
            h.append([dist,[px, py]])
        heapq.heapify(h)
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res