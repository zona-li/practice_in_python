from collections import deque


class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        charMap = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        q = deque([''])
        while len(q[0]) < len(digits):
            next = q.popleft()
            for c in charMap[int(digits[len(next)])]:
                q.append(next + c)
        return list(q)

s = Solution()
print(s.letterCombinations("232"))