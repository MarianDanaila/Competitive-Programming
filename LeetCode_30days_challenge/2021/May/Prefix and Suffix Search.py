from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        n = len(words)
        self.dct = {}
        for idx in range(n - 1, -1, -1):
            word = self.words[idx]
            len_word = len(word)
            for i in range(len_word):
                for j in range(len_word):
                    tpl = (word[:i + 1], word[j:])
                    if tpl not in self.dct:
                        self.dct[tpl] = idx

    def f(self, prefix: str, suffix: str) -> int:
        tpl = (prefix, suffix)
        if tpl in self.dct:
            return self.dct[tpl]
        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
