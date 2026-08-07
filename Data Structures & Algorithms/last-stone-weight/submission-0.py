import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = [-n for n in stones]
        count = len(stoneHeap)
        heapq.heapify(stoneHeap)
        while count > 1:
                stone1 = -1 * heapq.heappop(stoneHeap)
                stone2 = -1 * heapq.heappop(stoneHeap)
                result = abs(stone1 - stone2)
                heapq.heappush(stoneHeap,(-1 * result))
                count -= 1
        return -1 * stoneHeap[0]
