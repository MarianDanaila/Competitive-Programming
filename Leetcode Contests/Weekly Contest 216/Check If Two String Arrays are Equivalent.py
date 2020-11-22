class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        string1 = []
        string2 = []
        for word in word1:
            for ch in word:
                string1.append(ch)
        for word in word2:
            for ch in word:
                string2.append(ch)
        return string1 == string2
