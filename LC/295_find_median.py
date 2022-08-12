import bisect
import math

class MedianFinder:

  def __init__(self):
    self.nums = []

  def addNum(self, num: int) -> None:
    self.nums.insert(bisect.bisect(self.nums, num), num)

  def findMedian(self) -> float:
    indexes = len(self.nums) - 1
    if indexes % 2 == 0:
      return self.nums[int(indexes / 2)]
    else:
      left = math.floor(indexes / 2)
      right = math.ceil(indexes / 2)
      return (self.nums[left] + self.nums[right]) / 2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())