from typing import List


class Solution:
  def longestStrChain(self, words: List[str]) -> int:
    words.sort(key=lambda x: len(x))
    result = 1
    mem = {}
    for word in words:
      memed = mem.get(word)
      if memed:
        continue
      lenth = 1
      for idx in range(len(word)):
        new_word = word[0:idx] + word[idx+1:]
        new_memed = mem.get(new_word)
        if new_memed:
          lenth = max(lenth, new_memed + 1)
      mem[word] = lenth
      result = max(result, lenth)

    print(result)
    
          
s = Solution()
s.longestStrChain(["abcd","dbqca"])