from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = second = 0
        for c in cost:
            first, second = second, c + min(first, second)
        return min(first, second)
