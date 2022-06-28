from typing import List


class Solution:
  def __init__(self) -> None:
    self.matrix = [[]]
    self.max_i = 0
    self.max_j = 0

  def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    max_i, max_j = len(matrix), len(matrix[0])
    self.matrix = matrix
    self.max_i = max_i
    self.max_j = max_j
    if max_j == 0 or max_i == 0:
      return 0
    ans = 0
    mem = [[0 for _ in range(max_j)] for _ in range(max_i)]
    for i in range(max_i):
      for j in range(max_j):
        ans = max(ans, self.travel(i, j, mem))
    return ans

  def travel(self, i, j, mem):
    if mem[i][j] != 0:
      return mem[i][j]
    options = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    for (r, c) in options:
      if 0 <= r < self.max_i and 0 <= c < self.max_j and self.matrix[r][c] > self.matrix[i][j]:
        mem[i][j] = max(mem[i][j], self.travel(r, c, mem))

    mem[i][j] = mem[i][j] + 1
    return mem[i][j]


sol = Solution()
print(sol.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
