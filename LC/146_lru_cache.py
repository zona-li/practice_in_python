from collections import deque


class LRUCache:

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.count = 0
    self.lru = deque([])
    self.dict = {}

  def get(self, key: int) -> int:
    if key not in self.dict:
      return -1
    self.lru.remove(key)
    self.lru.append(key)
    return self.dict[key]

  def put(self, key: int, value: int) -> None:
    if key in self.dict:
      self.dict[key] = value
      self.lru.remove(key)
      self.lru.append(key)
      return
    
    if self.count < self.capacity:
      self.count += 1
    else:
      toBeRemoved = self.lru.popleft()
      del self.dict[toBeRemoved]

    self.dict[key] = value
    self.lru.append(key)
        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2, 1)
obj.put(2, 2)
print(obj.get(2))
obj.put(1, 1)
obj.put(4, 1)
print(obj.get(2))