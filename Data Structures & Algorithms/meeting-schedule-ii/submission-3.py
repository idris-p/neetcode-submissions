"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x.start)
        result = [intervals[0].end]

        for interval in intervals[1:]:
            if interval.start >= result[0]:
                heapq.heappop(result)
            heapq.heappush(result, interval.end)

        return len(result)
