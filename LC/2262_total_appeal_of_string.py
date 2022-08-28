import bisect
from collections import defaultdict
from operator import indexOf


class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        indexDict = defaultdict(list)
        for i, c in enumerate(s):
            indexDict[c].append(i)

        sumAppeal = 0
        for i, c in enumerate(s):
            pos = indexOf(indexDict[c], i)
            leftPos = indexDict[c][pos - 1] if pos > 0 else -1
            sumAppeal += (i - leftPos) * (n - i)

        return sumAppeal

s = Solution()
print(s.appealSum("abbca"))
