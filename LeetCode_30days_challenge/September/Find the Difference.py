from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        for ch in s:
            freq_t[ch] -= 1
            if freq_t[ch] == 0:
                freq_t.pop(ch)
        for key in freq_t:
            return key
