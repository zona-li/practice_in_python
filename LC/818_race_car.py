class Solution:
  def __init__(self) -> None:
    self.dp = {0: 0}

  def racecar(self, target: int) -> int:
    if target in self.dp:
      return self.dp[target]

    n = target.bit_length()
    if 2**n - 1 == target:
      self.dp[target] = n
    else:
      path_count = n + 1 + self.racecar(2**n - 1 - target)
      for m in range(n - 1):
        path_count = min(path_count, n + m + 1 + self.racecar(target - 2**(n - 1) + 2**m))
      self.dp[target] = path_count

    return self.dp[target]



a = Solution()
print(a.racecar(5))