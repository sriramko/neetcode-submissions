"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    meetings = []
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        busy = set()
        for interval in intervals:
            for i in range(interval.start,interval.end):
                if i not in busy:
                    busy.add(i)
                else:
                    return False
        return True;