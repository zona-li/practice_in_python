from collections import defaultdict
from typing import List


class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    wordMark = '*'

    root = {}
    for w in words:
      curr = root
      for c in w:
        curr = curr.setdefault(c, {})
      curr[wordMark] = w

    rows = len(board)
    cols = len(board[0])

    result = []

    def explore(i, j, node):
      c = board[i][j]
      curr = node[c]
      if wordMark in curr:
        result.append(curr[wordMark])
        del curr[wordMark]

      board[i][j] = '#'
      for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
        if x >= 0 and y >= 0 and x < rows and y < cols and board[x][y] in curr:
          explore(x, y, curr)
      board[i][j] = c

      if not curr:
        del node[c]
      
    for i in range(rows):
      for j in range(cols):
        if board[i][j] in root:
          explore(i, j, root)

    return result

    

s = Solution()
print(s.findWords(
  [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
  ["oath","pea","eat","rain"]
))




