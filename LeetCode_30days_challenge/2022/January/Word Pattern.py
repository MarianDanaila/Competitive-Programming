class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(s)
        bijection = {}
        start_word = end_word = 0
        used = set()
        for ch in pattern:
            if end_word == n + 1:
                return False
            while end_word < n and s[end_word] != ' ':
                end_word += 1
            word = s[start_word:end_word]
            end_word += 1
            start_word = end_word
            if ch not in bijection:
                if word in used:
                    return False
                bijection[ch] = word
                used.add(word)
            else:
                if bijection[ch] != word:
                    return False

        return end_word == n + 1
