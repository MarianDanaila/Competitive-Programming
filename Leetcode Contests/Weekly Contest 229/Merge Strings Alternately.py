class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        n = len(word1)
        m = len(word2)
        for i in range(min(n, m)):
            merged.append(word1[i])
            merged.append(word2[i])
        i += 1
        while i < n:
            merged.append(word1[i])
            i += 1

        while i < m:
            merged.append(word2[i])
            i += 1

        return "".join(merged)
