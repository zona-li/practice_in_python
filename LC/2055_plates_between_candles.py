import bisect
from typing import List
from unittest import result


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        count = 0
        leftBound = False
        candles = []
        counts = []
        for i, c in enumerate(s):
            if c == '*':
                if leftBound:
                    count += 1
            else:
                leftBound = True
                candles.append(i)
                counts.append(count)
        results = []
        for left, right in queries:
            leftIndex = bisect.bisect_left(candles, left)
            if leftIndex >= len(candles) or left == right:
                results.append(0)
                continue
            rightIndex = bisect.bisect_left(candles, right)
            if rightIndex == len(candles) or candles[rightIndex] != right:
                rightIndex -= 1
            plates = counts[rightIndex] - counts[leftIndex]
            if plates >= 0:
                results.append(plates)
            else:
                results.append(0)
        print(candles, counts)
        return results


    def platesBetweenCandles(self, s, queries):
        A = [i for i,c in enumerate(s) if c == '|']
        res = []
        for a,b in queries:
            i = bisect.bisect_left(A, a)
            j = bisect.bisect(A, b) - 1
            res.append((A[j] - A[i]) - (j - i) if i < j else 0)
        return res

s = Solution()

print(s.platesBetweenCandles("*|*|||", [[0,0],[1,3]]))
