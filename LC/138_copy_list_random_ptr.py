# Definition for a Node.
from typing import Optional


class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random

class Solution:
  def __init__(self) -> None:
    self.visited = {}

  def copyNode(self, node):
    if not node:
      return node
    if node in self.visited:
      return self.visited[node]
    else:
      newNode = Node(node.val)
      self.visited[node] = newNode
      return newNode

  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
      return head
    oldNode = head
    newNode = self.copyNode(head)
    newHead = newNode

    while oldNode:
      newNode.next = self.copyNode(oldNode.next)
      newNode.random = self.copyNode(oldNode.random)

      oldNode = oldNode.next
      newNode = newNode.next
    
    return newHead
    