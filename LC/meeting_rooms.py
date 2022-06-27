import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
      sorted_timeline = self.sort_interval(intervals)
      rooms = []
      maxRooms = 0
      for i, interval in enumerate(sorted_timeline):
        if i == 0:
          heapq.heappush(rooms, interval[1])
          maxRooms += 1
        else:
          end_time = rooms[0]
          if end_time <= interval[0]:
            heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])
          else:
            maxRooms += 1
            heapq.heappush(rooms, interval[1])
      return len(rooms)

    def sort_interval(self, intervals: List[List[int]]) -> int:
      return sorted(intervals, key=lambda interval: (interval[0], interval[1]))
