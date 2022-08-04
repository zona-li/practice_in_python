from collections import deque
from typing import List


class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordList = set(wordList)
    if endWord not in wordList:
      return 0
    candidates = deque([[beginWord, 1]])
    while candidates:
      word, length = candidates.popleft()
      if word == endWord:
        return length
      for i in range(len(word)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
          next_word = word[:i] + c + word[i+1:]
          if next_word in wordList:
            wordList.remove(next_word)
            candidates.append([next_word, length + 1])

    return 0
    
    

  def oneAppart(self, a: str, b: str) -> bool:
    len_a = len(a)
    if len_a != len(b):
      return False
    diffCount = 0
    for ptr in range(len_a):
      if a[ptr] != b[ptr]:
        diffCount += 1
      if diffCount > 2:
        return False
    return diffCount == 1
    

s = Solution()
print(s.ladderLength("ymain", "oecij", ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]))