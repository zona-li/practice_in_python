
class Solution:
    def numberOfWays(self, s: str) -> int:
        ways = {'0': 0, '1': 0, '01': 0, '10': 0, '101': 0, '010': 0}
        for c in s:
            if c == '0':
                ways['0'] += 1
                ways['10'] += ways['1']
                ways['010'] += ways['01']
            else:
                ways['1'] += 1
                ways['01'] += ways['0']
                ways['101'] += ways['10']
        return ways['101'] + ways['010']

s = Solution()
print(s.numberOfWays('111100111'))

