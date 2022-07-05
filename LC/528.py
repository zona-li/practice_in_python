import random
from typing import List


class Solution:
  def __init__(self, w: List[int]):
    # w = [4, 5, 2, 3]
    prob = []
    max = 0
    for num in w:
      max += num
      prob.append(max)
    self.prob = prob
    self.max = prob[len(prob) - 1]

  def pickIndex(self) -> int:
    len_arr = len(self.prob)
    randomInt = random.randint(0, self.max - 1)
    print(self.prob, randomInt)
    left, right = 0, len_arr
    while left < right:
      mid = left + (right - left) // 2 
      if randomInt > self.prob[mid]:
        left = mid + 1
      else:
        right = mid

    return left

s = Solution([1, 3])
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())
print(s.pickIndex())

