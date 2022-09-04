from abc import ABC, abstractmethod
from typing import List 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class OpNode(Node):
    def __init__(self, val = '', l: Node = None, r: Node = None) -> None:
        self.val = val
        self.left = l
        self.right = r

    def evaluate(self) -> int:
        if self.val == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.val == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == '/':
            return self.left.evaluate() // self.right.evaluate()

class NumNode(Node):
    def __init__(self, val = '') -> None:
        self.val = val

    def evaluate(self) -> int:
        return int(self.val)

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        ops = ['+', '-', '*', '/']
        for c in postfix:
            if c in ops:
                rt = stack.pop()
                lt = stack.pop()
                node = OpNode(c, lt, rt)
                stack.append(node)
            else:
                node = NumNode(c)
                stack.append(node)
        return stack[0]

        
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        