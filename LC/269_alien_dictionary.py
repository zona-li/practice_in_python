from typing import List


class Solution:
  def alienOrder(self, words: List[str]) -> str:
    adj = { c : set() for w in words for c in w }

    for idx in range(len(words) - 1):
      w1, w2 = words[idx], words[idx + 1]
      min_len = min(len(w1), len(w2))
      if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
        return ""
      for i in range(min_len):
        if w1[i] != w2[i]:
          adj[w1[i]].add(w2[i])
          break

    res = []
    visit = {}
    def search(c):
      if c in visit:
        return visit[c]

      visit[c] = True
      for neighbor in adj[c]:
        if search(neighbor):
          return ""
      visit[c] = False
      res.append(c)

    for c in adj:
      if search(c):
        return ""

    res.reverse()
    return "".join(res)


s = Solution()
print(s.alienOrder(["z","x","z"]))