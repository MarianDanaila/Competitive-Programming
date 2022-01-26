class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = not_capitals = first_capital = False
        if 'A' <= word[0] <= 'Z':
            first_capital = True
        else:
            not_capitals = True
        n = len(word)
        for i in range(1, n):
            ch = word[i]
            if 'A' <= ch <= 'Z':
                capitals = True
            else:
                not_capitals = True
        return not not_capitals or not capitals or (first_capital and not capitals)
