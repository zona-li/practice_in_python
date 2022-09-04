from collections import Counter


class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        count = Counter(s)
        if max(count['0'], count['1']) > min(count['0'], count['1']) + 1:
            return -1
        n = len(s)
        res = [0] * 2
        for i in range(0, n, 2):
            res[0] += s[i] == '0'
            res[1] += s[i] == '1'
        if count['0'] == count['1']:
            return min(res)
        if count['0'] < count['1']:
            return res[0]
        else:
            return res[1]