from collections import defaultdict, deque

import math


class Solution:
  def countOfAtoms(self, formula: str) -> str:
    counts = defaultdict(int)
    q = deque(formula)

    multipliers = deque()
    count = ''
    atom = ''
    num_right_parentheses = 0

    while len(q):
      next = q.pop()
      if num_right_parentheses == 0:
        if next.isnumeric():
          count = next + count
        if next.islower():
          atom = next + atom
        if next.isupper():
          atom = next + atom
          if len(count) == 0:
            count = '1'
          counts[atom] += int(count)
          atom = ''
          count = ''
        if next == ')':
          num_right_parentheses += 1
          if len(count) == 0:
            count = '1'
          multipliers.append(int(count))
          count = ''
      else:
        if next.isnumeric():
          count = next + count
        if next == '(':
          num_right_parentheses -= 1
          multipliers.pop()
        if next == ')':
          num_right_parentheses += 1
          if len(count) == 0:
            count = '1'
          multipliers.append(int(count))
          count = ''
        if next.islower():
          atom = next + atom
        if next.isupper():
          atom = next + atom
          if len(count) == 0:
            count = '1'
          total_count = int(count) * math.prod(multipliers)
          counts[atom] += total_count
          count = ''
          atom = ''
    
    res = ''
    for atom in sorted(counts.keys()):
      res += atom
      if counts[atom] > 1:
        res += str(counts[atom])
    return(res)

a = Solution()
print(a.countOfAtoms("H2O"))