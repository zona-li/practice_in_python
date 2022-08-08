import bisect


class Solution:
    def suggestedProducts(self, A, word):
        A.sort()
        res, prefix = [], ''
        for c in word:
            prefix += c
            i = bisect.bisect_left(A, prefix)
            res.append([w for w in A[i:i + 3] if w.startswith(prefix)])
        return res

s = Solution()
print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))

# ['mobile', 'moneypot', 'monitor', 'mouse', 'mousepad']