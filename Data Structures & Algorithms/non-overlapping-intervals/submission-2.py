class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval:interval[0])
        if len(intervals) < 2:
            return 0
        oLength = len(intervals)
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] > intervals[i+1][0]: #overlap
                intersect = [intervals[i+1][0],min(intervals[i][1],intervals[i+1][1])]
                del intervals[i]
                del intervals[i]
                intervals.insert(i,intersect)
            else:
                i += 1
        return oLength - len(intervals)