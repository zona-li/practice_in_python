

class Solution:
  def calculate(self, s: str) -> int:
    priorityOps = ['*', '/']
    ops = ['+', '-', '*', '/']
    stack = []
    num = ''
    needEval = False
    for c in s:
      if c in ops:
        stack.append(int(num))
        num = ''
        if needEval:
          needEval = False
          second = stack.pop()
          operator = stack.pop()
          value = self.evaluate(stack.pop(), operator, second)
          stack.append(value)
        stack.append(c)
        if c in priorityOps:
          needEval = True
      elif c != ' ':
        num += c
    if num:
      stack.append(int(num))
      if needEval:
        second = stack.pop()
        operator = stack.pop()
        value = self.evaluate(stack.pop(), operator, second)
        stack.append(value)

    prev = None
    op = ''
    for value in stack:
      if value in ops:
        op = value
      elif prev == None:
        prev = value
      else:
        prev = self.evaluate(prev, op, value)
      
    return prev

  def evaluate(self, first: int, op: str, second: int) -> int:
    if op == '+':
      return first + second
    elif op == '-':
      return first - second
    elif op == '*':
      return first * second
    elif op == '/':
      return first // second

s = Solution()
print(s.calculate("0-2147483647"))