from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        set_words = set(words)
        length = 0
        for word in words:
            length_word = len(word)
            for i in range(1, length_word):
                set_words.discard(word[i:])

        for word in set_words:
            length += (len(word) + 1)
        return length
