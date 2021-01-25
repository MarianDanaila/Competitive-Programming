class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        i1 = i2 = j1 = j2 = 0
        while i1 < len(word1) and i2 < len(word2):
            if word1[i1][j1] != word2[i2][j2]:
                return False
            if j1 == len(word1[i1]) - 1:
                i1 += 1
                j1 = 0
            else:
                j1 += 1

            if j2 == len(word2[i2]) - 1:
                i2 += 1
                j2 = 0
            else:
                j2 += 1

        return i1 == len(word1) and i2 == len(word2)
