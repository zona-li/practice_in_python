from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxDamage, totalDamage = 0, 0
        for d in damage:
            if d > maxDamage:
                maxDamage = d
            totalDamage += d
        saved = min(armor, maxDamage)
        return totalDamage - saved + 1

s = Solution()
print(s.minimumHealth([3,3,3], 0))
