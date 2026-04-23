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
        
        if len(intervals) < 1:
            return 0
            
        meeting_rooms = []
        intervals = sorted(intervals, key = lambda x: x.start)
        meeting_rooms.append(intervals[0].end) 
        heapq.heapify(meeting_rooms)

        for i in intervals[1:]:
            start, end = i.start, i.end
            earliest_room = meeting_rooms[0]
            if earliest_room <= start:
                heapq.heappop(meeting_rooms)
            heapq.heappush(meeting_rooms, end)
        
        return len(meeting_rooms)

