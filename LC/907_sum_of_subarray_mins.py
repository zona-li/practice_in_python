from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        array = [float('-inf')] + arr + [float('-inf')]
        stack = []
        sum = 0
        for i, num in enumerate(array):
            while stack and num < array[stack[-1]]:
                minNumIndex = stack.pop()
                sum += array[minNumIndex] * (minNumIndex - stack[-1]) * (i - minNumIndex)
                sum = sum % (10 ** 9 + 7)
            stack.append(i)
        return sum

s = Solution()
print(s.sumSubarrayMins([11,81,94,43,3]))