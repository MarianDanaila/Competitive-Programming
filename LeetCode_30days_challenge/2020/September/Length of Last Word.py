class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = False
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if word:
                    return length
                else:
                    continue
            else:
                word = True
                length += 1
        return length
