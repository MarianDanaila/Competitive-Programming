from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = Counter(s)
        for ch in t:
            if ch not in counter:
                return False
            else:
                counter[ch] -= 1
                if counter[ch] == 0:
                    counter.pop(ch)

        return True
