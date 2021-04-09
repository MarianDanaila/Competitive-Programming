from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}
        for i in range(26):
            alphabet[order[i]] = i
        n = len(words)
        for i in range(n - 1):
            len1 = len(words[i])
            len2 = len(words[i + 1])
            min_len = min(len1, len2)
            good = False
            for j in range(min_len):
                if alphabet[words[i][j]] > alphabet[words[i + 1][j]]:
                    return False
                elif alphabet[words[i][j]] < alphabet[words[i + 1][j]]:
                    good = True
                    break
            if not good and len1 > len2:
                return False
        return True
