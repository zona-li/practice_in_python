import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      num_to_letters = collections.defaultdict(list)
      for str in strs:
        num_to_letters[tuple(sorted(str))].append(str)
      return num_to_letters.values


sol = Solution()
sol.groupAnagrams([","])
