from typing import List


class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for token in tokens:
      if len(stack) == 0:
        stack.append(token)
      elif self.isOperand(token):
        b = stack.pop()
        a = stack.pop()
        num = self.calc(a, b, token)
        stack.append(num)
      else:
        stack.append(token)
    return stack.pop()

  def calc(self, a, b, eval) -> int:
    int_a, int_b = int(a), int(b)
    if eval == '/':
      return int(int_a / int_b)
    elif eval == '*':
      return int_a * int_b
    elif eval == '-':
      return int_a - int_b
    elif eval == '+':
      return int_a + int_b

  def isOperand(self, string) -> bool:
    return string in ['/', '*', '+', '-']


s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))