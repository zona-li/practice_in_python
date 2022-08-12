from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        res = []
        words_dict = set(words)
        for word in words:
            words_dict.remove(word)
            if self.check(word, words_dict) is True:
                res.append(word)
            words_dict.add(word)
        return res

    def check(self, word, d):
        if word in d:
            return True

        for i in range(len(word), 0, -1):
            if word[:i] in d and self.check(word[i:], d):
                return True

        return False


s = Solution()
print(s.findAllConcatenatedWordsInADict(
    ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))
