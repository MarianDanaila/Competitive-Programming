class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        dct = {}
        for i in range(len(s)):
            if s[i] <= t[i]:
                diff = ord(t[i]) - ord(s[i])
                try:
                    dct[diff] += 1
                except KeyError:
                    dct[diff] = 1
            else:
                diff = 26 - (ord(s[i]) - ord(t[i]))
                try:
                    dct[diff] += 1
                except KeyError:
                    dct[diff] = 1
        maxim = 0
        for el in dct:
            if el == 0:
                continue
            maxim = max(el + (26 * (dct[el] - 1)), maxim)
        return maxim <= k

