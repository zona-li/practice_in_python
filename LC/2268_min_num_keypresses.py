from collections import Counter, defaultdict


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count = Counter(s)
        letters = count.most_common()
        numDict = defaultdict(int)
        curr = 1
        res = 0
        for _, sum in letters:
            numDict[curr] += 1
            res += sum * numDict[curr]
            curr += 1
            if curr > 9:
                curr = 1
        return res

s = Solution()
print(s.minimumKeypresses('abcdefghijkl'))