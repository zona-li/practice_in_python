# Definition for a binary tree node.
from collections import deque


class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def expTree(self, s: str) -> 'Node':
        stack = deque(list(s))
        return self.parseExpression(stack)

    def parseExpression(self, stack: deque):
        lhs = self.parseTerm(stack)
        while stack and stack[0] in ['+', '-']:
            op = stack.popleft()
            rhs = self.parseTerm(stack)
            lhs = Node(op, lhs, rhs)
        return lhs

    def parseTerm(self, stack: deque):
        lhs = self.parsePhrase(stack)
        while stack and stack[0] in ['*', '/']:
            op = stack.popleft()
            rhs = self.parsePhrase(stack)
            lhs = Node(op, lhs, rhs)
        return lhs

    def parsePhrase(self, stack: deque):
        if stack[0] == '(':
            stack.popleft()
            node = self.parseExpression(stack)
            stack.popleft()
            return node
        else:
            val = stack.popleft()
            return Node(val)


s = Solution()
print(s.expTree("5*2-3+9/(5-2)+1"))