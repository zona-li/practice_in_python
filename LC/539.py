def findMinDifference(self, timePoints):
        t = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        t.append(t[0] + 1440)
        return min(b - a for a, b in zip(t, t[1:]))