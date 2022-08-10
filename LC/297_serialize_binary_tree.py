
from collections import deque
from turtle import right
from typing import Optional


class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Codec:

  def serialize(self, root: Optional[TreeNode]):
    resultArr = []
    if not root:
      return ''
    q = deque([root])
    while q:
      next = q.popleft()
      if not next:
        resultArr.append('None')
      else:
        resultArr.append(str(next.val))
        q.append(next.left)
        q.append(next.right)
    return ','.join(resultArr)

  def deserialize(self, data: str):
    if not data:
      return None
    nodevals = deque(data.split(','))
    root = TreeNode(int(nodevals.popleft()))
    processed = deque([root])
    while processed:
      next = processed.popleft()
      leftVal = nodevals.popleft()
      rightVal = nodevals.popleft()
      leftNode = TreeNode(leftVal) if leftVal != 'None' else None
      rightNode = TreeNode(rightVal) if rightVal != 'None' else None
      next.left = leftNode
      next.right = rightNode
      if leftNode:
        processed.append(leftNode)
      if rightNode:
        processed.append(rightNode)
    return root