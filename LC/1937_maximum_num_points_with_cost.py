from typing import List


class Solution:
  def maxPoints(self, points: List[List[int]]) -> int:
    rows = len(points)
    columns = len(points[0])

    if rows == 1:
      return max(points[0])
    if columns == 1:
      return sum(r[0] for r in points)

    def left_max(arr):
      res = [arr[0]] + [0] * (columns - 1)
      for i in range(1, columns):
        res[i] = max(res[i - 1] - 1, arr[i])
      return res

    def right_max(arr):
      res = [0] * (columns - 1) + [arr[columns - 1]]
      for i in range(columns - 2, -1, -1):
        res[i] = max(res[i + 1] - 1, arr[i])
      return res

    prev = points[0]
    for i in range(1, rows):
      left, right = left_max(prev), right_max(prev)
      curr = [0] * columns
      for j, val in enumerate(points[i]):
        curr[j] = val + max(left[j], right[j])
      prev = curr[:]
    return max(prev)



s = Solution()
print(s.maxPoints([[1,5],[2,3],[4,2]]))