from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        lowLen = len(str(low))
        highLen = len(str(high))
        for n in range(lowLen, highLen + 1):
            for i in range(1, 11 - n):
                num = i
                for j in range(n - 1):
                    num = num * 10 + (i + j + 1)
                if num >= low:
                    if num <= high:
                        res.append(num)
                    else:
                        break
        return res

s = Solution()
print(s.sequentialDigits(124, 3456))