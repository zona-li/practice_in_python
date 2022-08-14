from typing import List


class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = {c: [] for c in range(numCourses)}
    for a, b in prerequisites:
      graph[a].append(b)

    visited, visiting = [], []
    def dfs(c):
      if c in visited:
        return True
      if c in visiting:
        return False

      visiting.append(c)
      for prerequisite in graph[c]:
        if dfs(prerequisite) == False:
          return False

      visiting.remove(c)
      visited.append(c)
      return True

    for c in graph.keys():
      if dfs(c) == False:
        return False
    return True

s = Solution()
print(s.canFinish(2, [[1, 0], [0, 1]]))