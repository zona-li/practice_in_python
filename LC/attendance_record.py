class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        if n == 0:
            return 0
        if n == 1:
            return 3
        res = [1, 2, 4]
        for i in range(3, n + 1):
          res.append((res[i - 1] + res[i - 2] + res[i - 3]) % mod)
        num = res[n]
        print(num)
        for i in range(1, n + 1):
            num += (res[i - 1] * res[n - i]) % mod
        num %= mod
        return num


s = Solution()
print(s.checkRecord(2))
