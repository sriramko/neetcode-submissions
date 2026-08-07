class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                i += 1
                continue
            elif intervals[i][0] > newInterval[1]:
                intervals.insert(i, newInterval)
                return intervals
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
                del intervals[i]
        intervals.append(newInterval)
        return intervals
