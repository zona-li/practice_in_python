from curses.ascii import SO
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            newArr = []
            for i in range(len(nums) - 1):
                newArr.append((nums[i] + nums[i + 1]) % 10)
            nums = newArr
        return nums[0]

s = Solution()
print(s.triangularSum([5]))