class Solution:
  def calculate(self, s: str) -> int:
    result, curr = 0, 0
    num, op = '', ''
    sign = 'pos'
    for c in s:
      if c in ['+', '-']:
        if sign == 'neg':
          result -= self.compute(curr, int(num), op)
        else:
          result += self.compute(curr, int(num), op)
        curr = 0
        sign = 'neg' if c == '-' else 'pos'
        num = ''
        op = ''
      elif c in ['*', '/']:
        if not op:
          curr = int(num)
        else:
          curr = self.compute(curr, int(num), op)
        num = ''
        op = c
      elif c:
        num += c
    if sign == 'neg':
      result -= self.compute(curr, int(num), op)
    else:
      result += self.compute(curr, int(num), op)
    return result

  def compute(self, a, b, op):
    if op == '+':
      return a + b
    elif op == '-':
      return a - b
    elif op == '*':
      return a * b
    elif op == '/':
      return a // b
    else:
      return a + b

s = Solution()
print(s.calculate("0-2147483647"))