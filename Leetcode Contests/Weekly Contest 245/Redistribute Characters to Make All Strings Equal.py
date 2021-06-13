from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        """
            To redistribute characters equally we need the occurrence of every character to be divided exactly to the
            number of words
        """
        n = len(words)
        characters = {}
        for word in words:
            for ch in word:
                if ch not in characters:
                    characters[ch] = 1
                else:
                    characters[ch] += 1

        for ch in characters:
            if characters[ch] % n != 0:
                return False
        return True
