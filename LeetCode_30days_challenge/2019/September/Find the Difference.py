# Approach 1 using HashMap
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        for ch in s:
            freq_t[ch] -= 1
            if freq_t[ch] == 0:
                freq_t.pop(ch)
        for key in freq_t:
            return key

# Approach 2 using Bit Manipulation (XOR)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = ord(t[-1])
        for i in range(len(s)):
            xor ^= ord(s[i])
            xor ^= ord(t[i])
        return chr(xor)