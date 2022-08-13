from typing import List

class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = {c: [] for c in range(numCourses)}
    for c, pre in prerequisites:
      graph[c].append(pre)

    result = []
    visited, visiting = [], []
    def dfs(c):
      if c in visiting:
        return False
      if c in visited:
        return True
      
      visiting.append(c)
      for pre in graph[c]:
        if not dfs(pre):
          return False
      
      visiting.remove(c)
      visited.append(c)
      result.append(c)
      return True

    for c in graph.keys():
      if not dfs(c):
        return []

    return result


s = Solution()
print(s.findOrder(1, []))