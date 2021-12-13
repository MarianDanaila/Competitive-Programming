class Solution:
    def maxPower(self, s: str) -> int:
        power = length = 1
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                length += 1
            else:
                power = max(power, length)
                length = 1

        return max(power, length)
