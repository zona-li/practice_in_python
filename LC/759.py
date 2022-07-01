import bisect

class Interval:
  def __init__(self, start: int = None, end: int = None):
    self.start = start
    self.end = end

class Solution:
  def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    work_intervals = []
    for interval in schedule[0]:
      start = interval.start
      end = interval.end
      work_intervals.append(start)
      work_intervals.append(end)
    for p in range(1, len(schedule)):
      for time in schedule[p]:
        start, end = time.start, time.end
        left_idx = bisect.bisect_left(work_intervals, start)
        right_idx = bisect.bisect_right(work_intervals, end)
        insert = []
        if left_idx % 2 == 0:
          insert.append(start)
        if right_idx % 2 == 0:
          insert.append(end)
        work_intervals[left_idx:right_idx] = insert
    free_intervals = []
    next = Interval()
    for idx, time in enumerate(work_intervals):
      if idx == 0:
        continue
      if idx % 2 == 1:
        next.start = time
      else:
        next.end = time
        free_intervals.append(next)
        next = Interval()
    return free_intervals

# Second solution:
'''
class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res, end = [], ints[0].end
        for i in ints[1:]:
            if i.start > end:
                res.append(Interval(end, i.start))
            end = max(end, i.end)
        return res
'''
