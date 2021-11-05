from math import sqrt


class Solution:
    def arrangeCoins(self, n: int) -> int:
        delta = 8 * n + 1
        return int((sqrt(delta) - 1) / 2)
