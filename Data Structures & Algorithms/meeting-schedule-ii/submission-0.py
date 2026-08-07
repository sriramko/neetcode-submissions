"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        numDays = 0
        freq = dict()
        for interval in intervals:
            for i in range(interval.start,interval.end):
                freq[i] = 1 + freq.get(i,0)
                numDays = max(freq[i],numDays)
        return numDays