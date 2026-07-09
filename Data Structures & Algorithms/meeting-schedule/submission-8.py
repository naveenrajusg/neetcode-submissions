"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i:i.start)
        if len(intervals)==0:
            return True

        tracked = [intervals[0].start,intervals[0].end]

        for indexes in intervals[1:]:
            start, end = indexes.start, indexes.end
            if start<tracked[1]:
                return False
            else:
                tracked = [start,end]

        return True