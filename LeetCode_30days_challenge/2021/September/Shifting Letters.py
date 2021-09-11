from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix_shifts = [shifts[-1]]
        n = len(s)
        for i in range(n - 2, -1, -1):
            prefix_shifts.append(prefix_shifts[-1] + shifts[i])
        shifted = []
        for i in range(n):
            shifted.append(chr((ord(s[i]) - 97 + prefix_shifts[n - i - 1]) % 26 + 97))
        return "".join(shifted)
