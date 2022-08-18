# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getNum(self, s: str):
        if len(s) == 0:
            return (None, '')
        i = 0
        while s[i].isnumeric():
            i += 1
        return (int(s[0:i]), s[i:])

    def expTree(self, s: str) -> 'Node':
        nextNum, restStr = self.getNum(s)
        print(nextNum, restStr)


s = Solution()
s.expTree("3*4-2*5")
