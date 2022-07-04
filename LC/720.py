from collections import defaultdict
from typing import List

class TrieNode:
  def __init__(self, value = None) -> None:
    self.value = value
    self.children = defaultdict(TrieNode)

class Solution:
  def longestWord(self, words: List[str]) -> str:
    max = []
    root = TrieNode()
    words.sort(key=lambda x: (len(x), x))
    for word in words:
      if len(word) == 1:
        root.children[word] = TrieNode(word)
        if len(max) == 0 or len(max[0]) == 1:
          max.append(word)

      else:
        node = root
        for idx, c in enumerate(list(word)):
          if not node.children[c].value:
            if idx != len(word) - 1:
              break
            else:
              node.children[c] = TrieNode(c)
              if len(max) == 0:
                max.append(word)
              else:
                prev = max[0]
                if len(prev) < len(word):
                  max = [word]
                elif len(prev) == len(word):
                  max.append(word)
          else:
            node = node.children[c]

    if len(max) == 0:
      return ""
    elif len(max) > 1:
      max.sort()
      return max[0]
    else:
      return max[0]
          
s = Solution()
print(s.longestWord(["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]))