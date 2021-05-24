class Solution:
    def toLowerCase(self, s: str) -> str:
        lowercase = []
        for ch in s:
            if 'A' <= ch <= 'Z':
                lowercase.append(chr(ord(ch) + 32))
            else:
                lowercase.append(ch)
        return "".join(lowercase)
