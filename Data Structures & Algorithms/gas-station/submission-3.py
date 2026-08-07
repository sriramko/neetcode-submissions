class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        running = 0
        best = 0
        for i in range(len(gas)):
            running += gas[i] - cost[i]
            if gas[i] - cost[i] > 0 and gas[i - 1] - cost[i - 1] < 0:
                best = i
        if running < 0:
            return -1
        else:
            return best

