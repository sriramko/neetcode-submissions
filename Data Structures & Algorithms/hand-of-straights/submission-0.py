class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0) # default value of 0 if not already in map
        minH = list(count.keys())
        heapq.heapify(minH) # linear time
        #setup

        while minH:
            first = minH[0] # min value at top of heap
            for i in range(first,first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
        