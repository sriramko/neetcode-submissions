class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v,w))
        
        minHeap = [(0, k)]
        visit = set()
        best = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            else:
                visit.add(n1)
                best = max(best, w1)
                for n2, w2 in edges[n1]:
                    if n2 not in visit:
                        heapq.heappush(minHeap, (w1 + w2, n2))

        return best if len(visit) == n else -1

