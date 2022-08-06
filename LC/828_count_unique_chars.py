import string

class Solution:
  def uniqueLetterString(self, s: str) -> int:
    pos = {l: [-1, -1] for l in string.ascii_uppercase}
    res = 0
    for i, c in enumerate(s):
      j, k = pos[c]
      res += (k - j) * (i - k)
      pos[c] = [k, i]
    for c in pos:
      j, k = pos[c]
      res += (k - j) * (len(s) - k)
    return res % (10**9 + 7)

a = Solution()
print(a.uniqueLetterString("ABA"))
