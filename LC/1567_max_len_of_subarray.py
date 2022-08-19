from collections.abc import MutableSequence
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        i, j = 0, 0
        maxLen = 0
        negIndex = -1
        carryNeg = False
        while j < len(nums):
            if nums[j] < 0:
                if negIndex < 0:
                    negIndex = j
                if not carryNeg:
                    carryNeg = True
                    maxLen = max(maxLen, j - i)
                else:
                    carryNeg = False
                    maxLen = max(maxLen, j - i + 1)
            elif nums[j] == 0:
                if not carryNeg:
                    maxLen = max(maxLen, j - i)
                else:
                    maxLen = max(maxLen, j - negIndex - 1)
                carryNeg = False
                negIndex = -1
                i = j + 1
            else:
                if not carryNeg:
                    maxLen = max(maxLen, j - i + 1)
                else:
                    maxLen = max(maxLen, j - negIndex)
            j += 1

        return maxLen

def getMaxLen(nums: List[int]) -> int:
    n = len(nums)
    pos, neg = 0, 0
    if nums[0] > 0: pos = 1
    if nums[0] < 0: neg = 1
    ans = pos
    for i in range(1, n):
        if nums[i] > 0:
            pos = 1 + pos
            neg = 1 + neg if neg > 0 else 0
        elif nums[i] < 0:
            pos, neg = 1 + neg if neg > 0 else 0, 1 + pos
        else:
            pos, neg = 0, 0
        ans = max(ans, pos)
    return ans

s = Solution()
print(getMaxLen([2, 3, -1,-4,-2,-3,0,1]))