"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(0, len(intervals)):
            for j in range(i + 1, len(intervals)):
                if not ((intervals[i].end <= intervals[j].start and intervals[i].end <= intervals[j].end) or (intervals[i].start >= intervals[j].start and intervals[i].start >= intervals[j].end)):
                    return False
        return True