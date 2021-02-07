class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                while s[i] == s[i + 1]:
                    i += 1
                    if i == j:
                        return 0
                while s[j] == s[j - 1]:
                    j -= 1
                    if i == j:
                        return 0
                i += 1
                j -= 1
            else:
                return j - i + 1
        return j - i + 1
