from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def enough(distance):
            count, i, j = 0, 0, 0
            n = len(nums)
            while i < n:
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                count += j - i - 1
                i += 1
            return count >= k

        nums = sorted(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if not enough(mid):
                left = mid + 1
            else:
                right = mid
        return left

s = Solution()
print(s.smallestDistancePair([1,3,1], 2))