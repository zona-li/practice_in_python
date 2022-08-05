from collections import Counter, defaultdict
from itertools import combinations
from typing import List


class Solution:
  def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    data = sorted(list(zip(username, timestamp, website)))
    users = defaultdict(list)
    for user, _, web in data:
      users[user].append(web)
    
    pattern = Counter()
    for web in users.values():
      pattern.update(Counter(set(combinations(web, 3))))

    return list(sorted(pattern.items(), key=lambda item: (-item[1], item[0]))[0][0])


s = Solution()
print(s.mostVisitedPattern(
  ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"],
  [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930],
  ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]
))
      


