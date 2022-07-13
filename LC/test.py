

from concurrent.futures import process


def findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax):
  left, right = 0, 1
  numProcessors = len(bootingPower)
  res = 0
  maxBootingPow = bootingPower[0]
  proPow = processingPower[0]
  
  while right < numProcessors:
    currPower = maxBootingPow + proPow
    if currPower < powerMax:
      res = max(res, right - left)
      maxBootingPow = max(maxBootingPow, bootingPower[right])
      proPow = proPow / (right - left) * (right - left + 1) + processingPower[right] * (right - left + 1)
      right += 1
    elif currPower == powerMax:
      return right - left
    else:
      if right == left + 1:
        left += 1
        right += 1
        maxBootingPow = bootingPower[left]
        proPow = processingPower[left]
      else:
        left += 1
        maxBootingPow = max(bootingPower[left:right])
        proPow = proPow / (right - left + 1) * (right - left)

  return res


print(findMaximumSustainableClusterSize([2, 1, 3, 4, 5], [3, 6, 1, 3, 4], 25))