import bisect


class SORTracker:

    def __init__(self):
        self.locations = []
        self.count = 0

    def add(self, name: str, score: int) -> None:
        idx = bisect.bisect_left(self.locations, (-score, name))
        self.locations.insert(idx, (-score, name))

    def get(self) -> str:
        res = self.locations[self.count]
        self.count += 1
        return res[1]
