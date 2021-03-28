from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        digits = [0] * 10
        counter = Counter(s)
        letter_to_digit = {'g': ["eight", 8], 'x': ["six", 6], 'u': ["four", 4], 'w': ["two", 2], 'z': ["zero", 0],
                           's': ["seven", 7], 'v': ["five", 5], 'h': ["three", 3], 'i': ["nine", 9], 'o': ["one", 1]}

        for letter in letter_to_digit:
            digit = letter_to_digit[letter][0]
            index = letter_to_digit[letter][1]
            if letter in counter:
                freq = counter[letter]
                if freq > 0:
                    digits[index] += freq
                    for ch in digit:
                        counter[ch] -= freq
        ans = []
        for i in range(10):
            if digits[i] > 0:
                ans.append(str(i) * digits[i])
        return "".join(ans)
