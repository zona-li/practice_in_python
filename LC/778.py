from cgitb import small
from email import header
from typing import List
import heapq

class Solution:
  def swimInWater(self, grid: List[List[int]]) -> int:
    n = len(grid)
    first = grid[0][0]
    seen = [first]
    q = [(first, 0, 0)]
    ans = 0
    while len(q):
      next, i, j = heapq.heappop(q)
      ans = max(ans, next)
      if i == j == n - 1:
        return ans
      for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= x < n and 0 <= y < n and grid[x][y] not in seen:
          heapq.heappush(q, (grid[x][y], x, y))
          seen.append(next)
    return ans

a = Solution()
print(a.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))