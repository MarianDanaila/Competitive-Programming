from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)
        dct = {}
        for ch in c2:
            freq = c2[ch]
            if freq not in dct:
                dct[freq] = 1
            else:
                dct[freq] += 1
        for ch in c1:
            if ch not in c2:
                return False
            else:
                freq = c1[ch]
                if freq not in dct or dct[freq] == 0:
                    return False
                dct[freq] -= 1
        return True
