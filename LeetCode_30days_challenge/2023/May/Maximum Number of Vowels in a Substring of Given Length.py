class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        max_vowels = curr_vowels = 0
        for i in range(n):
            if s[i] in "aeiou":
                curr_vowels += 1
            if i - k >= 0:
                if s[i - k] in "aeiou":
                    curr_vowels -= 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels
