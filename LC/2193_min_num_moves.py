from shutil import move


class Solution:
    def minMovesToMakePalindrome(self, s):
        s = list(s)
        res = 0
        while s:
            i = s.index(s[-1])
            if i == len(s) - 1:
                res += int(i / 2)
            else:
                res += i
                s.pop(i)
            s.pop()
        return res

s = Solution()
print(s.minMovesToMakePalindrome('abba'))