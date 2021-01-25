class Solution:
    def maxPower(self, s: str) -> int:
        power = length = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                length += 1
            else:
                power = max(power, length)
                length = 1

        return max(power, length)
