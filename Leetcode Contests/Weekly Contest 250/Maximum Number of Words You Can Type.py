class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_letters = set()
        for ch in brokenLetters:
            broken_letters.add(ch)
        counter = 0
        words = text.split(" ")
        for word in words:
            good = True
            for ch in word:
                if ch in broken_letters:
                    good = False
                    break
            if good:
                counter += 1

        return counter
