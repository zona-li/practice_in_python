from typing import List

class Node:
  def __init__(self) -> None:
    self.children = {}
    self.isEnd = False
    self.value = None
    self.rank = 0


class AutocompleteSystem:

  def __init__(self, sentences: List[str], times: List[int]):
    self.root = Node()
    self.search_str = ""
    for idx, string in enumerate(sentences):
      self.populate(string, times[idx])

  def populate(self, value, rank):
    curr = self.root
    for c in value:
      if c not in curr.children:
        curr.children[c] = Node()
      curr = curr.children[c]
    curr.isEnd = True
    curr.rank -= rank
    curr.value = value

  def store_search(self):
    self.populate(self.search_str, 1)

  def search(self):
    curr = self.root
    for c in self.search_str:
      if c not in curr.children:
        return []
      else:
        curr = curr.children[c]
    return self.dfs(curr)

  def dfs(self, node: Node):
    result = []
    if node:
      if node.isEnd:
        result.append((node.rank, node.value))
      for c in node.children:
        result.extend(self.dfs(node.children[c]))
    return result

  def input(self, c: str) -> List[str]:
    result = []
    if c != '#':
      self.search_str += c
      search_result = self.search()
      sorted_result = sorted(search_result, key=lambda x: (x[0], x[1]))
      result = [r[1] for r in sorted_result[:3]]
    else:
      self.store_search()
      self.search_str = ""
    return result

