from typing import List


class Solution:
  def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: (x[1], x[0]), reverse=True)
    count, i = 0, 0
    units = 0
    while count < truckSize and i < len(boxTypes):
      numBox, numUnitsPerBox = boxTypes[i]
      numBoxLeft = truckSize - count
      if numBoxLeft >= numBox:
        count += numBox
        units += numBox * numUnitsPerBox
        i += 1
      else:
        count = truckSize
        units += numBoxLeft * numUnitsPerBox
    return units

s = Solution()
print(s.maximumUnits([[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]], 35))
