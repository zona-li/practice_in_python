import bisect
class SnapshotArray:
  def __init__(self, length: int):
    self.a = [[[-1, 0]] for _ in range(length)]
    self.id = 0

  def set(self, index: int, val: int) -> None:
    self.a[index].append([self.id, val])

  def snap(self) -> int:
    self.id += 1
    return self.id - 1

  def get(self, index: int, snap_id: int) -> int:
    i = bisect.bisect(self.a[index], [snap_id + 1]) - 1
    return self.a[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(4)
id0 = obj.snap()
id1 = obj.snap()
print(obj.get(3, 1))
obj.set(2, 4)
id3 = obj.snap()
obj.set(1, 4)
print(obj.get(1, id3))