from opcode import hasfree
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        hasFresh = 0
        rottens = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hasFresh += 1
                elif grid[i][j] == 2:
                    rottens.append((i, j))
        if not hasFresh:
            return 0
        timer = 0
        nextBatch = set()

        while rottens:
            i, j = rottens.pop()
            for a, b in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if a >= 0 and b >= 0 and a < m and b < n and grid[a][b] == 1:
                    grid[a][b] = 2
                    hasFresh -= 1
                    nextBatch.add((a, b))
            if not rottens:
                timer += 1
                rottens = list(nextBatch)
                nextBatch.clear()
        return -1 if hasFresh else timer - 1


s = Solution()
print(s.orangesRotting([[0, 2]]))
