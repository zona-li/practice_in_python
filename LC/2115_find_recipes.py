# recipes = ["burger", "sandwich", "bread"]
# ingredients = [["sandwich","meat","bread"],["bread","meat"],["yeast","flour"]]
# supplies = ["yeast","flour","meat"]

from collections import Counter, defaultdict, deque
from typing import List

from traitlets import default


class Solution:
  def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    adj = defaultdict(set)
    indegree = defaultdict(int)

    for rec, ings in zip(recipes, ingredients):
      for ing in ings:
        adj[ing].add(rec)
        indegree[rec] += 1

    res = []
    q = deque(supplies)
    while len(q):
      next = q.popleft()
      if next in recipes:
        res.append(next)

      for rec in adj[next]:
        indegree[rec] -= 1
        if indegree[rec] == 0:
          q.append(rec)

    return res





s = Solution()
print(s.findAllRecipes(["burger", "sandwich", "bread"], [["sandwich","meat","bread"],["bread","meat"],["yeast","flour"]], ["yeast","flour","meat"]))

