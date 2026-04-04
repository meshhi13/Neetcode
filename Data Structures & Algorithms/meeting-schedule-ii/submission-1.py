"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda x: x.start)

        count = 1 if intervals else 0
        i = 0
        while intervals:
            if i >= len(intervals):
                count += 1
                i = 0

            end = intervals.pop(i).end
            while i < len(intervals) and intervals[i].start < end:
                i += 1

        return count