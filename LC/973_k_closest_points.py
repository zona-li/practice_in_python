import heapq
from typing import List


class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for x, y in points:
      dis = x ** 2 + y ** 2
      heapq.heappush(heap, (dis, x, y))
    res = []
    for _ in range(k):
      next = heapq.heappop(heap)
      res.append([next[1], next[2]])
    return res

s = Solution()
print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))