from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        n = len(pattern)
        ans = []
        for word in words:
            bij = {}
            good = True
            for i in range(n):
                if word[i] in bij:
                    if bij[word[i]] != pattern[i]:
                        good = False
                        break
                else:
                    if pattern[i] in bij.values():
                        good = False
                        break
                    bij[word[i]] = pattern[i]

            if good:
                ans.append(word)
        return ans
