# recipes = ["burger", "sandwich", "bread"]
# ingredients = [["sandwich","meat","bread"],["bread","meat"],["yeast","flour"]]
# supplies = ["yeast","flour","meat"]

from typing import List


class Solution:
  def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    mem = {}
    for supply in supplies:
      mem[supply] = True
    result = []
    for idx, recipe in enumerate(recipes):
      if mem.get(recipe):
        result.append(recipe)
        continue
      q = ingredients[idx]
      canMake = True
      while len(q) and canMake:
        next = q.pop()
        available = mem.get(next)
        if available:
          continue
        in_recipes = next in recipes
        if not available and not in_recipes:
          canMake = False
          break
        if in_recipes:
          index = recipes.index(next)
          q.extend(ingredients[index])
      if canMake:
        mem[recipe] = True
        result.append(recipe)
      else:
        mem[recipe] = False

    return result





s = Solution()
print(s.findAllRecipes(["burger", "sandwich", "bread"], [["sandwich","meat","bread"],["bread","meat"],["yeast","flour"]], ["yeast","flour","meat"]))

