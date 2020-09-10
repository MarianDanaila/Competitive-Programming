from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        freq = Counter(secret)
        counter = Counter(guess)
        used = []
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
                freq[secret[i]] -= 1
                counter[guess[i]] -= 1
                used.append(i)
        for i in range(len(guess)):
            if freq[guess[i]] > 0 and counter[guess[i]] > 0:
                freq[guess[i]] -= 1
                counter[guess[i]] -= 1
                cows += 1
        return str(bulls) + 'A' + str(cows) + 'B'
