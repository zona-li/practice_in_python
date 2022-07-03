
from collections import defaultdict
from typing import List, Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    trees = defaultdict(list)
    ids = defaultdict()
    ids.default_factory = ids.__len__
    
    def getId(node: TreeNode):
      if node:
        id = ids[getId(node.left), node.val, getId(node.right)]
        trees[id].append(node)
        return id

    getId(root)
    return [n[0] for n in trees.values() if n[1:]]
