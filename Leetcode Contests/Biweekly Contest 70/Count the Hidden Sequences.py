from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        hidden = [0] * (n + 1)
        hidden[-1] = lower
        minim = maxim = lower
        for i in range(n - 1, -1, -1):
            hidden[i] = hidden[i + 1] - differences[i]
            minim = min(minim, hidden[i])
            maxim = max(maxim, hidden[i])
        return max(upper - maxim - (lower - 1 - minim), 0)
