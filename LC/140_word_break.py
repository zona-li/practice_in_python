from typing import List


class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    mem = {}

    def dfs(word: str):
      result = []
      if word in mem:
        return mem[word]

      for w in wordDict:
        if word.startswith(w):
          if len(word) == len(w):
            result += [w]
          else:
            for y in dfs(word[len(w):]):
              result += [w + ' ' + y]
      
      mem[word] = result
      return result

    return dfs(s)


s = Solution()
print(s.wordBreak('aaaaaaa', ["aaaa","aa","a"]))