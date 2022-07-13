from collections import defaultdict
import heapq


class StockPrice:

  def __init__(self):
    self.latest = 0
    self.latest_tmp = 0
    self.minMap = []
    self.maxMap = []
    self.track = defaultdict(list)

  def update(self, timestamp: int, price: int) -> None:
    self.track[timestamp].append(price)
    heapq.heappush(self.minMap, (price, timestamp))
    heapq.heappush(self.maxMap, (-price, timestamp))
    if timestamp >= self.latest_tmp:
      self.latest = price
      self.latest_tmp = timestamp

  def current(self) -> int:
    return self.latest

  def maximum(self) -> int:
    next = self.maxMap[0]
    while abs(next[0]) != self.track[next[1]][len(self.track[next[1]]) - 1]:
      heapq.heappop(self.maxMap)
      next = self.maxMap[0]
    return abs(next[0])

  def minimum(self) -> int:
    next = self.minMap[0]
    while next[0] != self.track[next[1]][len(self.track[next[1]]) - 1]:
      heapq.heappop(self.minMap)
      next = self.minMap[0]
    return next[0]


stockPrice = StockPrice()
stockPrice.update(1, 10) # Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5)  # Timestamps are [1,2] with corresponding prices [10,5].
print(stockPrice.current())     # return 5, the latest timestamp is 2 with the price being 5.
print(stockPrice.maximum())     # return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3)  # The previous timestamp 1 had the wrong price, so it is updated to 3.
                          # Timestamps are [1,2] with corresponding prices [3,5].
print(stockPrice.maximum())     # return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2)  # Timestamps are [1,2,4] with corresponding prices [3,5,2].
print(stockPrice.minimum())   # return 2, the minimum price is 2 at timestamp 4.