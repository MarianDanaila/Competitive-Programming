class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        counter = 0
        for ch in word:
            if 'A' <= ch <= 'Z':
                counter += 1
        return counter == 0 or counter == len(word) or (counter == 1 and 'A' <= word[0] <= 'Z')
