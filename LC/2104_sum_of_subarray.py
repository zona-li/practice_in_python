from typing import List


class Solution:
  def subArrayRanges(self, A0):
    res = 0
    inf = float('inf')
    A = [-inf] + A0 + [-inf]
    s = []
    for i, x in enumerate(A):
      while s and A[s[-1]] > x:
        j = s.pop()
        k = s[-1]
        res -= A[j] * (i - j) * (j - k)
      s.append(i)
        
    A = [inf] + A0 + [inf]
    s = []
    for i, x in enumerate(A):
      while s and A[s[-1]] < x:
        j = s.pop()
        k = s[-1]
        res += A[j] * (i - j) * (j - k)
      s.append(i)
    return res

s = Solution()
print(s.subArrayRanges([9, 12, 11, 6, 3, 7, 10]))
